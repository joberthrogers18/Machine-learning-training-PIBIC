import requests as req
import youtube_dl
from youtube_transcript_api import YouTubeTranscriptApi
from pydub import AudioSegment
import uuid
import os

def get_videos(keyword):

    api_key_youtube = 'AIzaSyAlg5R2U3a3rpxGlsrDSdDdmS9nksfBQeY'
    keyword = 'teste software'

    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={keyword}&maxResults=25&key=' + api_key_youtube
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
    drugs_subtitle = []
    subtitles = YouTubeTranscriptApi.get_transcript(video_id)

    for subtitle in subtitles:
        if keyword in subtitle['text']:
            drugs_subtitle.append(subtitle)

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
    sound = AudioSegment.from_file('CHORO FÁCIL - STAND UP-sdVabHZnU7g.wav') 
    first_half = sound[ start * 1000 : end * 1000 - 2000]
    first_half.export(f"aux_{count}.wav", format="wav")

if __name__ == '__main__':
    videos = get_videos('maconha')
    
    for video in videos:
        download(f'https://www.youtube.com/watch?v={video}')
        subtitles = get_subtitle(video)

        count = 0

        for subtitle in subtitles:
            split_audio(subtitle['start'], subtitle['start'] + subtitle['duration'], count)
            count += 1

        # integration api speech recognition google

        remove_aux_wavs()