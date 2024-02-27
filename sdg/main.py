import argparse
import os
import requests

from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

def send(name, artist, album, file):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, "..", "assets")
    sent_files = []
    for file_name in os.listdir(assets_dir):
        file_path = os.path.join(assets_dir, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as file:
                    url = "http://localhost:8080/audio/insert"
                    files = {"audioFile": (file_name, file)}
                    data = {
                        "name": name,
                        "artist": artist,
                        "album": album
                    }
                    response = requests.post(url, files=files, data=data)
                    if response.status_code != 200:
                        print("Failure:", response.text, name, artist, album)
                    else:
                        print("Success:", response.text, name, artist, album)
                        sent_files.append(file_path)
            except IOError as e:
                print("Error opening file:", e)

def main():
    parser = argparse.ArgumentParser(description="A music command-line generator")
    parser.add_argument("-d", "--description", help="description of audio to generate")
    parser.add_argument("-n", "--name", help="name of audio to generate")
    parser.add_argument("-a", "--artist", help="artist of audio to generate")
    parser.add_argument("-l", "--album", help="album of audio to generate")
    parser.add_argument("-t", "--time", default=5, help="Total seconds of audio to generate")
    args = parser.parse_args()
    if args.description != None and args.description != "":
        print('Generating Music Description:', args.description)
        model = MusicGen.get_pretrained('facebook/musicgen-small')
        model.set_generation_params(duration=int(args.time))  # generate total seconds
        descriptions = [args.description]
        wav = model.generate(descriptions)
        for idx, one_wav in enumerate(wav):
            file_name = f'assets/{idx}_{args.name}_{args.artist}_{args.album}'
            audio_write(file_name, one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)
            send(args.name, args.artist, args.album, file_name)


if __name__ == "__main__":
    main()
