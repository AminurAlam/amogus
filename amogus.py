import requests
import os
import argparse

# Configure this if the search results are not enough for you
SEARCH_LIMIT = 25

# API URL
API_URL = 'https://itunes.apple.com/'

# Logo
LOGO = r"""
  __ _ _ __ ___   ___   __ _ _   _ ___
 / _` | '_ ` _ \ / _ \ / _` | | | / __|
( (_| | | | | | | (_) | (_| | |_| \__ \
 \__,_|_| |_| |_|\___/ \__, |\__,_|___/
repository:             __/ |Ver: 1.0.0
github.com/R3AP3/amogus|___/           
"""


def download_artwork(url, filename):
    r = requests.get(url)
    if r.status_code == 200:
        ext = r.headers['Content-Type'].split('/')[1]
        if ext == 'jpeg':
            ext = 'jpg'
        with open(f'cover/{filename}.{ext}', 'wb') as f:
            f.write(r.content)
    else:
        print('Error downloading artwork [' + str(r.status_code) + ']')


def request(request_action, params):
    r = requests.get(API_URL + request_action, params=params)
    return r.json()


def search(search_input, search_type):
    params = {
        'term': search_input,
        'entity': search_type,
        'limit': SEARCH_LIMIT
    }
    return request('search', params)


def lookup(lookup_input, region):
    params = {
        'id': lookup_input,
        'country': region,
        'entity': 'album',
        'limit': 200,
        'sort': 'recent'
    }
    lookup_info = request('lookup', params)
    for result in lookup_info['results']:
        if result['wrapperType'] == 'collection':
            print(f"{result['collectionName']} [{result['collectionId']}]")
            artwork_url = 'https://a1.mzstatic.com/r40/' + '/'.join(result['artworkUrl100'].split('/')[5:-1])
            filename = f"{result['artistId']} - {result['collectionId']}"
            download_artwork(artwork_url, filename)
        elif result['wrapperType'] == 'artist':
            print(f"Downloading Artist: {result['artistName']} [{result['artistId']}]")


def url_parse(url):
    split_url = url.split('/')
    if split_url[3] == 'artist' or split_url[3] == 'album':
        return split_url[-1], 'us', split_url[3]
    else:
        return split_url[-1], split_url[3], split_url[4]


def main(args):
    if args.search:
        if args.artist_search:
            shit = ['musicArtist', 'artistId', 'artistName']
        else:
            shit = ['album', 'collectionId', 'collectionName']
        results = search(args.input, shit[0])['results']
        for i in range(len(results)):
            print(f"[{i + 1}] {results[i][shit[2]]} [{results[i][shit[1]]}]")
        choice = input("\nChoice: ")
        if choice.isdigit():
            choice = int(choice) - 1
            lookup(results[choice][shit[1]], args.region_code)
    else:
        adam_id, region, lookup_type = url_parse(args.input)
        lookup(adam_id, region)


if __name__ == "__main__":
    print(LOGO)
    if not os.path.exists("cover"):
        os.makedirs("cover")
    parser = argparse.ArgumentParser(
        description="Downloads Album Covers as their Source File from the Itunes Search API"
    )
    parser.add_argument(
        "-s", "--search",
        dest='search',
        help="Search for Albums",
        action="store_true"
    )
    parser.add_argument(
        "-a", "--artist",
        dest='artist_search',
        help="Search for Artist (use in combination with --search)",
        action="store_true"
    )
    parser.add_argument(
        "-r", "--region",
        type=str, dest='region_code',
        help="Set Region Code [Default: 'us'] (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)",
        default="us",
        metavar="REGION_CODE"
    )
    parser.add_argument(
        "input",
        type=str,
        help="Apple Music URL or Search Query",
        metavar="INPUT"
    )
    main(parser.parse_args())
    print("Done")
