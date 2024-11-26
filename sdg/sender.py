import os
import shutil
import requests
from sdg.audio import Audio
from sdg.config import UNSENT, SENT


class Sender:

    def __init__(self):
        pass


    def send(self):
        for filename in os.listdir(UNSENT):
            if self._do(filename, os.path.join(UNSENT, filename)):
                self._move(filename)


    def _do(self, file_name: str, file_path: str) -> bool:
        if not file_name.endswith('.wav'):
            print("file type not supported")
            return
        try:
            print("sending payloads")
            audio = Audio(description=file_name)
            with open(file_path, 'rb') as file:
                url = 'http://localhost:8082/audio/insert'
                files = {'audioFile': (file_name, file)}
                response = requests.post(url, files=files, data=audio.__dict__)
                if response.status_code != 200:
                    print('Failure:', response.text,
                          audio.name, audio.artist, audio.album)
                    return False
                else:
                    print('Success:', response.text,
                          audio.name, audio.artist, audio.album)
                    return True
        except IOError as e:
            print('Error opening file:', e)
            return False


    def _move(self, filename):
        source_path = os.path.join(UNSENT, filename)
        destination_path = os.path.join(SENT, filename)
        shutil.move(source_path, destination_path)


if __name__ == '__main__':
    Sender().send()
