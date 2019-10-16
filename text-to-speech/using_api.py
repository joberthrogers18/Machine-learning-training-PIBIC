import requests as req
import youtube_dl
from youtube_transcript_api import YouTubeTranscriptApi
from pydub import AudioSegment
import uuid
import os
import io

# from google.cloud import speech
# from google.cloud.speech_v1 import enums
# from google.cloud.speech import types
# from google.oauth2 import service_account

def get_videos(keyword):

    api_key_youtube = 'AIzaSyAlg5R2U3a3rpxGlsrDSdDdmS9nksfBQeY'
    # keyword = 'teste software'

    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={keyword}&maxResults=3&key=' + api_key_youtube
    resp = req.get(url)
    data = resp.json()

    save_ids = []

    try:
        for video in data['items']:
            save_ids.append(video['id']['videoId'])
    except KeyError:
        pass

    return save_ids

def get_subtitle(video_id, keyword):
    print('passou')
    
    drugs_subtitle = []

    try:
        subtitles = YouTubeTranscriptApi.get_transcript(video_id)

        for subtitle in subtitles:
            if keyword in subtitle['text']:
                drugs_subtitle.append(subtitle)
    except:
        pass

    return drugs_subtitle


def download(link):
    print("Link detectado...")
    print("O video " + link + " será baixado")
    opts = {
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '50'
        }]
    }
    youtube_dl.YoutubeDL(opts).download([link])

def remove_aux_wavs():
    files = os.listdir(os.getcwd())

    for item in files:
        if item.endswith(".wav"):
            os.remove(os.path.join(os.getcwd(), item))

def split_audio(start, end, count):
    name_file = f"aux_{count}.wav"
    sound = AudioSegment.from_file('CHORO FÁCIL - STAND UP-sdVabHZnU7g.wav') 
    splited_audio = sound[ start * 1000 : end * 1000 - 2000]
    splited_audio.export(name_file, format="wav")

    return name_file

# def google_ST_process(file_aux):
#     file_name = os.path.join(
#         os.path.dirname(__file__),
#         file_)

def split_audio_single(list_audio, keyword):
    for voice in list_audio:
        sound = AudioSegment.from_file(voice)
        # splited_audio = sound[api['start']: api['end']]
        # splited_audio.export(f'/dataset/{keyword}-{uuid.uuid1()}.wav', format="wav")

if __name__ == '__main__':
    keyword = 'maconha'
    videos = get_videos(keyword)
    subtitles = []

    for video in videos:
        download(f'https://www.youtube.com/watch?v={video}')
        subtitles = get_subtitle(video, keyword)

        count = 0
        list_aux_audios = []

        # for subtitle in subtitles:
        #     list_aux_audios.append(
        #         split_audio(
        #             subtitle['start'], 
        #             subtitle['start'] + subtitle['duration'], 
        #             count
        #         )
        #     )
        #     count += 1
        
        # print(list_aux_audios)
        
        # split_audio_single(list_aux_audios, keyword) # integration api speech recognition google

        # remove_aux_wavs()



    #client = speech.SpeechClient()

    # # The name of the audio file to transcribe
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'maconha.mp3')

    # # Loads the audio into memory
    # with io.open(file_name, 'rb') as audio_file:
    #     content = audio_file.read()
    #     audio = types.RecognitionAudio(content=content)

    # config = speech.types.RecognitionConfig( encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16, language_code='pt-BR',  audio_channel_count=2)
    # print(config)

    # # Detects speech in the audio file
    # response = client.recognize(config, audio)

    # print(response)

    # for result in response.results:
    #     print('Transcript: {}'.format(result.alternatives[0].transcript))