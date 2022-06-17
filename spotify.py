#spotify API top 500 rolling stones album project
#regex class="c-gallery-vertical__slide-wrapper" 500-0 -> c-gallery-vertical-album-title

import spotipy
import urllib, re

#functions:
#read url to file
#parse file to artist/album/song
#find songs on spotify and add to new playlist with spotipy
#profit?

url = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/"

f = urllib.request.urlopen(url)
file = f.readlines()
for line in file:
    print(line)


class Song():

    def __init__(self, Title = None, Artist = None, Album = None, rank = None):
        self.Title = Title
        self.Artist = Artist
        self.Album = Album
        self.rank = rank


def read_file(file):

    return file

def parse_file(file):

    return

def make_playlist():


def add_to_playlist():


def main():


if __init__ == __main__:
    main()
