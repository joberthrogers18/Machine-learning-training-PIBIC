# observação: para rodar esse script é necessário criar uma chave de autenticação
# com .json para conexão desse programa com a api
# Se tiver com o .json de autenticação, rode: "export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account_file.json"
# mais informações em: https://stackoverflow.com/questions/38703853/how-to-use-google-speech-recognition-api-in-python

import argparse
import base64
import json

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')


def get_speech_service():
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build(
        'speech', 'v1', http=http, discoveryServiceUrl=DISCOVERY_URL)


def main(speech_file):
    """Transcribe the given audio file.

    Args:
        speech_file: the name of the audio file.
    """
    with open(speech_file, 'rb') as speech:
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().recognize(
        body={
            'config': {
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                'sampleRateHertz': 16000,  # 16 khz
                'languageCode': 'en-US',  # a BCP-47 language tag
                'enableWordTimeOffsets': True
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    response = service_request.execute()
    print(json.dumps(response))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'speech_file', help='Full path of audio file to be recognized')
    args = parser.parse_args()
    main(args.speech_file)