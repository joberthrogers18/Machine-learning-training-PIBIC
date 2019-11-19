import os
from pydub import AudioSegment
import uuid

if __name__ == '__main__':

    for audio in os.listdir(os.getcwd() + "/aux"):
        current_audio = AudioSegment.from_mp3("aux/" + audio)
        current_audio.export("fumar/" + "fumar_" + uuid.uuid4().hex +".wav", format="wav")
