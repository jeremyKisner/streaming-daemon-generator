import argparse
import asyncio
from sdg.streaming_daemon_generator import execute


def main():
    parser = argparse.ArgumentParser(
        description='a music command-line generator')
    parser.add_argument('-d', '--description', default='piano',
                        help='description of audio to generate')
    parser.add_argument('-n', '--name', default='',
                        help='name of audio to generate')
    parser.add_argument('-a', '--artist', default='',
                        help='artist of audio to generate')
    parser.add_argument('-l', '--album', default='',
                        help='album of audio to generate')
    parser.add_argument('-t', '--time', default=15,
                        help='total seconds of audio to generate')
    parser.add_argument('-s', '--storage', default=True,
                        help='enable to forward save results to storage api')
    args = parser.parse_args()
    asyncio.run(execute(args))


if __name__ == '__main__':
    main()
