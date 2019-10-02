import os 
from gtts import gTTS
import pyttsx3 as ts
import random
import uuid

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

def treat_content_file (content_file):

  list_characters = ["!", ".", "'", "/", "|", "~", "`", 
  "@","#", "£", "$", "%", "^", "&", "*", "(", ")"]

  string_split = []

  for i in list_characters:
    content_file = content_file.replace(i, " ")

  string_split = content_file.split(" ")

  return string_split

if __name__ == '__main__':

  try:
    all_txts = find_txts()

    content_split = []

    try:
      os.mkdir(os.getcwd() + "/dataset")
    except (FileExistsError, OSError):
          pass

    useGttk = False

    # Init the default setup pyttsx3

    engine = ts.init()

    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')

    for filename in all_txts:
      
      file = open(filename, 'r')
      content_txt = file.read()
      content_split = treat_content_file(content_txt)

      for word in content_split:

        useGttk = bool(random.getrandbits(1))
        
        try:
          os.mkdir(os.getcwd() + "/dataset/" + word)
        except (FileExistsError, OSError):
          pass

        if useGttk:
          TTS = gTTS(text= word, lang='pt-br')
          TTS.save(f"dataset/{word}/{word}{uuid.uuid1()}.mp3")
        
        else:
          for voice in voices:
            if (voice.name == 'Luciana' or voice.name == 'Joana' ):
                engine.setProperty('voice', voice.id)
                engine.setProperty('rate', rate + random.randint(-15, 15))
                engine.setProperty('volume', volume - random.uniform(0.1, 0.9))
                engine.save_to_file(word, f"dataset/{word}/{word}{uuid.uuid1()}.mp3")


  except AssertionError:
    print('Não foi possível criar audios do texto atual!!')
