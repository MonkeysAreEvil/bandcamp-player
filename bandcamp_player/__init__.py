# coding=utf-8
import logging
import sys
import argparse

from bandcamp_parser.album import Album
from bandcamp_parser.tag import Tag
from bandcamp_parser.track import Track

logging.basicConfig(level=logging.INFO)


def loop():
    parser = argparse.ArgumentParser(description="Plays a track, an album, or random tracks from a tag, from Bandcamp.")
    parser.add_argument("--version", action="version", version="'%(prog)s 0.2.1'")
    any_of_required = parser.add_mutually_exclusive_group(required=True)
    any_of_required.add_argument("--album", help="plays an album")
    any_of_required.add_argument("--tag", help="plays random tracks with tag")
    any_of_required.add_argument("--track", help="plays a track")

    args = vars(parser.parse_args())

    album_url = args["album"]
    tag_url = args["tag"]
    track_url = args["track"]

    if album_url:
        album = Album(album_url)
        for track_url in album.tracks():
            track = Track(track_url)
            track.play()

    if tag_url:
        tag = Tag(sys.argv[2])
        while True:
            album_url = tag.album_random().href
            album = Album(album_url)
            track_url = album.track_random()
            track = Track(track_url)
            track.play()

    if track_url:
        track = Track(track_url)
        track.play()


def main():
    """ Playing the tracks until CTRL-C """
    try:
        loop()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
