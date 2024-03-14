from sdg.audio import Audio
import os
import requests
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write


def execute(audio: Audio):
    if audio.description != None and audio.description != '':
        print('Generating Music Description:', audio.description)
        model = MusicGen.get_pretrained('facebook/musicgen-small')
        model.set_generation_params(duration=int(15))
        wav = model.generate([audio.description])
        for idx, one_wav in enumerate(wav):
            file_name = f'assets/{idx}_{audio.name}_{audio.artist}_{audio.album}'
            audio_write(file_name, one_wav.cpu(), model.sample_rate,
                        strategy='loudness', loudness_compressor=True)
            send(audio, file_name)


def send(audio: Audio, file_name: str):
    assets_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'assets')
    sent_files = []
    for file_name in os.listdir(assets_dir):
        file_path = os.path.join(assets_dir, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'rb') as file:
                    url = 'http://localhost:8080/audio/insert'
                    files = {'audioFile': (file_name, file)}
                    data = {
                        'name': audio.name,
                        'artist': audio.artist,
                        'album': audio.album,
                        'description': audio.description,
                    }
                    response = requests.post(url, files=files, data=data)
                    if response.status_code != 200:
                        print('Failure:', response.text,
                              audio.name, audio.artist, audio.album)
                    else:
                        print('Success:', response.text,
                              audio.name, audio.artist, audio.album)
                        sent_files.append(file_path)
            except IOError as e:
                print('Error opening file:', e)
