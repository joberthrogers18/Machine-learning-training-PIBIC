
import os 
from gtts import gTTS

Text = "Meu parcerinho demais cara"

print("Espere... processando")
TTS = gTTS(text=Text, lang='pt-br')

TTS.save("voice.mp3")

os.system("start voice.mp3")
