from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath
import requests, re, os, shutil, time
os.system('cls' if os.name == 'nt' else 'clear')
logo="""
  __ _ _ __ ___   ___   __ _ _   _ ___ 
 / _` | '_ ` _ \ / _ \ / _` | | | / __|
| (_| | | | | | | (_) | (_| | |_| \__ \ 
 \__,_|_| |_| |_|\___/ \__, |\__,_|___/
Repo:                   __/ |Ver: 0.0.1
github.com/R3AP3/amogus|___/           
"""
print(logo)
while True:
    val = input("Apple Music URL: ")

    parts = PurePosixPath(unquote(urlparse(val).path)).parts
    album_id = parts[4]
    region_code = parts[1]

    response = requests.get(f'https://itunes.apple.com/lookup?id={album_id}&country={region_code}&entity=album')

    for details in response.json()["results"]:
        art_url = details["artworkUrl100"]
        art_name = details["artistName"]
        album_name = details["collectionName"]
        genre_name = details["primaryGenreName"]

    print(f'\nArtist:     {art_name}\nAlbum:      {album_name}\nGenre:      {genre_name}\nID:         {album_id}\n\nDownloading...\n')

    regex = r"/100x100bb.jpg"

    unc_png = "/100000x100000-100.png"
    unc_jpg = "/100000x100000-100.jpg"
    cp_webp = "/100000x100000-100.webp"

    png__url = re.sub(regex, unc_png, art_url, 1)
    jpg__url = re.sub(regex, unc_jpg, art_url, 1)
    webp_url = re.sub(regex, cp_webp, art_url, 1)

    path = f'C:\\Users\\admin\\Pictures\\CoverArtworks\\{album_name}\\'
    print(f"Saving to: {path}\n")
    os.mkdir(f'{path}')
    png_response = requests.get(png__url, stream=True)
    with open(f'{path}\\{album_name}.png', 'wb') as out_file:
        shutil.copyfileobj(png_response.raw, out_file)
    del png_response
    print("Best Quality     PNG     Done")

    jpg_res = requests.get(jpg__url, stream=True)
    with open(f'{path}\\{album_name}.jpg', 'wb') as out_file:
        shutil.copyfileobj(jpg_res.raw, out_file)
    del jpg_res
    print("Best Quality     JPG     Done")

    webp_res = requests.get(webp_url, stream=True)
    with open(f'{path}\\{album_name}.webp', 'wb') as out_file:
        shutil.copyfileobj(webp_res.raw, out_file)
    del webp_res
    print("Best Quality     WEBP    Done")

    print("\nSuccessfully Downloaded\n")
    time.sleep(3.0)
    os.system('cls' if os.name == 'nt' else 'clear')
