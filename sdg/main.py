from sdg.audio import Audio
from sdg.streaming_daemon_generator import execute
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='a music command-line generator')
    parser.add_argument('-d', '--description', default='',
                        help='description of audio to generate')
    parser.add_argument('-n', '--name', default='',
                        help='name of audio to generate')
    parser.add_argument('-a', '--artist', default='',
                        help='artist of audio to generate')
    parser.add_argument('-l', '--album', default='',
                        help='album of audio to generate')
    parser.add_argument('-t', '--time', default=15,
                        help='total seconds of audio to generate')
    args = parser.parse_args()
    execute(Audio(name=args.name, artist=args.artist,
            album=args.album, description=args.description))


if __name__ == '__main__':
    main()
