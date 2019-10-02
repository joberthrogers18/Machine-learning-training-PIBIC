

import pyttsx3 as ts
import random

engine = ts.init()

voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

for voice in voices:
    if (voice.name == 'Luciana' or voice.name == 'Joana' ):
        engine.setProperty('voice', voice.id)
        engine.setProperty('rate', rate + random.randint(-15, 15))
        engine.setProperty('volume', volume - random.uniform(0.1, 0.9))
        engine.say('Fala meu bom')

engine.runAndWait()
