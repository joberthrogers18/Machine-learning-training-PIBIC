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

import requests as req

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

print(save_ids)


