import speech_recognition as sr
# import pyaudio
# import pyttsx3
def listen():
    r = sr.Recognizer()
    mic = sr.Microphone.list_microphone_names()
    print(mic)


listen();