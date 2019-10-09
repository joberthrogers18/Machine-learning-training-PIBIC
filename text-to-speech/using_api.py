# import csv

# with open('all-maconha-tweets.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     line_count = 0
#     for row in csv_reader:

#         if line_count == 10: break

#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(row[2])
#             line_count += 1
#     print(f'Processed {line_count} lines.')

# import requests as req

# api_key_youtube = 'AIzaSyAlg5R2U3a3rpxGlsrDSdDdmS9nksfBQeY'
# keyword = 'teste software'

# url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={keyword}&maxResults=25&key=' + api_key_youtube
# resp = req.get(url)
# data = resp.json()

# save_ids = []

# try:
#     for video in data['items']:
#         save_ids.append(video['id']['videoId'])
# except KeyError:
#     pass

# print(save_ids)

import youtube_dl
from youtube_transcript_api import YouTubeTranscriptApi
from pydub import AudioSegment
import os

def get_subtitle(video_id):
    drugs_subtitle = []
    subtitles = YouTubeTranscriptApi.get_transcript(video_id)

    for subtitle in subtitles:
        if 'chorar' in subtitle['text']:
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
    first_half = sound[start * 1000 : end * 1000]
    first_half.export(f"aux_{count}.wav", format="wav")

if __name__ == '__main__':
    download('https://www.youtube.com/watch?v=sdVabHZnU7g')
    subtitles = get_subtitle('sdVabHZnU7g')
    print(subtitles)
    split_audio(subtitles[0]['start'], subtitles[0]['start'] + subtitles[0]['duration'], 0)

    remove_aux_wavs()