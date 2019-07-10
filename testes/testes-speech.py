import speech_recognition as sr

r = sr.Recognizer()

acting_so_weird = sr.AudioFile ('you-are-acting-so-weird.wav')

with acting_so_weird as source:
    audio = r.record(source)

print(r.recognize_google(audio))