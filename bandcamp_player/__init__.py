# coding=utf-8
import logging
import sys

from bandcamp_parser.album import Album
from bandcamp_parser.tag import Tag
from bandcamp_parser.track import Track

logging.basicConfig(level=logging.INFO)


def loop():
    usage = ("usage: bandcamp_player [-h | --help] --tag TAG | --track TRACK_URL | --album ALBUM_URL\n"
             "\n"
             "Plays a track, an album, or random tracks from a tag, from Bandcamp.\n"
             "\n"
             "Required arguments:\n"
             " any of --tag, --track, --album\n"
             "\n"
             "Optional arguments:\n"
             " -h, --help        show this help message and exit\n")

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(usage)
        exit(0)

    if sys.argv[1] == "--track":
        track = Track(sys.argv[2])
        track.play()
    elif sys.argv[1] == "--tag":
        tag_data = Tag(sys.argv[2])
        while True:
            album_url = tag_data.album_random().href
            album = Album(album_url)
            track_url = album.track_random()
            track = Track(track_url)
            track.play()
    elif sys.argv[1] == "--album":
        album = Album(sys.argv[2])
        for track_url in album.tracks():
            track = Track(track_url)
            track.play()
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(usage)
        exit(0)
    else:
        print(usage)
        exit(0)


def main():
    """ Playing the tracks until CTRL-C """
    try:
        loop()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
