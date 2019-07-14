import speech_recognition as sr

r = sr.Recognizer()

acting_so_weird = sr.AudioFile ('you-are-acting-so-weird.wav')

with acting_so_weird as source:
    # tentando tirar os ruidos do baralho
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

# show: True, retorna um JSON da api com todos os possiveis resultados
print(r.recognize_google(audio, show_all=True))