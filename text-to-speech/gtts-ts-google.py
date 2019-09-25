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

    for filename in all_txts:
      
      file = open(filename, 'r')
      content_txt = file.read()
      content_split = treat_content_file(content_txt)

      for word in content_split:
        
        try:
          os.mkdir(os.getcwd() + "/dataset/" + word)
        except (FileExistsError, OSError):
          pass

        TTS = gTTS(text= word, lang='pt-br')
        TTS.save(f"dataset/{word}/{word}.mp3")

  except AssertionError:
    print('Não foi possível criar audios do texto atual!!')
