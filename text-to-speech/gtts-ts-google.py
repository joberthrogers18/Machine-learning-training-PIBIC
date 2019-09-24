import os 
from gtts import gTTS

def filter_dirs(dirs):

  exclude = ['bin', 'include', 'lib', '.vscode']

  dirs[:] = [d for d in dirs if d not in exclude]
  return dirs

def find_txts():

  files_txt = []

  for root, dirs, files in os.walk(os.getcwd(), topdown=True):   
    dirs = filter_dirs(dirs)

    for file in files:
      if file.endswith('.txt'):
        print('passou')
        files_txt.append(os.path.join(root, file))

  return files_txt

if __name__ == '__main__':

  try:
    all_txts = find_txts()

    for filename in all_txts:
      file = open(filename, 'r')
      content_txt = file.read()
      print(content_txt)

    print("Espere... processando")
    TTS = gTTS(text='text', lang='pt-br')

    TTS.save("voice.mp3")

  except AssertionError:
    print('Não foi possível criar audios do texto atual!!')
