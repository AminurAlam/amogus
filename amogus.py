import json
import requests
import argparse

API_URL = 'https://itunes.apple.com/'  # API URL

def download_artwork(url, filename):
    r = requests.get(url)
    if r.status_code == 200:
        ext = r.headers['Content-Type'].split('/')[1]
        if ext == 'jpeg':
            ext = 'jpg'
        with open(f'{filename}.{ext}', 'wb') as f:
            f.write(r.content)
    else:
        print('Error downloading artwork [' + str(r.status_code) + ']')


def request(request_action, params):
    r = requests.get(API_URL + request_action, params=params)
    return r.json()


def lookup(lookup_input, region):
    lookup_info = request('lookup', {
        'id': lookup_input,
        'country': region,
        'entity': 'album',
        'limit': 200,
        'sort': 'recent'
    })
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
        return split_url[-1], 'us'
    else:
        return split_url[-1], split_url[3]


def main(args):
    if args.search:
        shit = ['musicArtist', 'artistId', 'artistName'] if args.artist_search else ['album', 'collectionId', 'collectionName']
        results = request('search', {
            'term': args.input, 'entity': shit[0], 'limit': args.limit
        })['results']
        for n, item in enumerate(results, start=1):
            print(json.dumps(item, indent=2))
            print(f"[{n}] {item[shit[2]]} [{item[shit[1]]}]")
        choice = input("\nChoice: ")
        if choice.isdigit():
            lookup(results[int(choice) - 1][shit[1]], args.region_code)
    else:
        lookup(*url_parse(args.input))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Downloads Album Covers as their Source File from the Itunes Search API")
    parser.add_argument("-s", "--search",
        dest='search', help="Search for Albums", action="store_true")
    parser.add_argument("-a", "--artist",
        help="Search for Artist (use in combination with --search)",
        dest='artist_search', action="store_true")
    parser.add_argument("-r", "--region",
        help="Set Region Code [Default: 'us'] (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)",
        type=str, dest='region_code', default="us", metavar="REGION_CODE")
    parser.add_argument("-l", "--limit",
        help="Configure this if the search results are not enough for you",
        type=int, default=5, metavar="NUM")
    parser.add_argument("input",
        help="Apple Music URL or Search Query", type=str, metavar="INPUT")

    main(parser.parse_args())
