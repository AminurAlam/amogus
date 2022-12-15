# Thats one sussy artwork Downloader
![amogus](https://user-images.githubusercontent.com/89069925/147856498-ce8049f1-1248-4f25-a425-da7dc9b404f7.jpg)

# Info [Last Update]:
I won't update this script anymore (as in adding new features) but if you encounter any bugs feel free to open an Issue or make a Pull Request.


## Usage:
This script will download artworks from Apple Music by using the Itunes search API.
The images will be the original file the artist or release provider provided to Apple Music.

Download Artwork:
```bash
python amogus.py https://music.apple.com/us/album/bad/559334659
```
Download all Artworks of an artist:
```bash
python amogus.py https://music.apple.com/us/album/bad/559334659
```
Search for an album:
```bash
python --search "Michael Jackson Thriller"
```
Search for an artist:
```bash
python --search --artist "Michael Jackson"
```

### Installing Amogus:
Install Python, this should work on any version. Then install the requirements:
```bash
git clone https://github.com/R3AP3/amogus.git amogus
cd amogus
pip install -r requirements.txt
```

## Changelog:
- 1.0.0: Initial Release (i just made up this version number)
  - Recoded the Script and made it more Stable
  - I just recoded it because it bugged me how bad this code was
  - removed Herobrine
  - added Sex
  
### Help:
```
usage: amogus.py [-h] [-s] [-a] [-r REGION_CODE] INPUT

Downloads Album Covers as their Source File from the Itunes Search API

positional arguments:
  INPUT                 Apple Music URL or Search Query

options:
  -h, --help            show this help message and exit
  -s, --search          Search for Albums
  -a, --artist          Search for Artist (use in combination with --search)
  -r REGION_CODE, --region REGION_CODE
                        Set Region Code [Default: 'us'] (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
```

###### i have no clue how to structure projects please god make it stop