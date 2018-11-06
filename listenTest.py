#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import time
import speech_recognition as sr
from responses import *


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

    try:
        rstring = str(r.recognize_google(audio))
        return rstring    # recognize speech using Google Speech Recognition - ONLINE
    except:                            # speech is unintelligible
        return handle(notFound)


def main():
    listen()

if __name__ == "__main__":
    main()