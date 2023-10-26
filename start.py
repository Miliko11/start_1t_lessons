import speech_recognition as sr
import pyaudio
import os
import webbrowser
import sys

def talk(words):
    print(words)

talk("Привет, чем я могу помочь вам?")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as sourse:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(sourse,duration=1)
        audio = r.listen(sourse)

    try:
        zadanie = r.recognize_google(audio,language="ru-Ru").lower()
        print("Вы сказали", zadanie)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = command()

    return zadanie

def Jarvis(zadanie):
    if 'программирование' in zadanie:
        talk("Уже открываю")
        url = 'https://start.1t.ru/c/index.html'
        webbrowser.open(url)
    elif 'аниме' in zadanie:
        url = 'https://animego.org/'
        webbrowser.open(url)
    elif 'стоп' in zadanie:
        talk("Да конечно, без проблем")
        sys.exit()
    elif 'имя' in zadanie:
        talk("Мое имя Jarvis")

while True:
    Jarvis(command())