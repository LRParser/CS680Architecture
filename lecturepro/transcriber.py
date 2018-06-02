#!/usr/bin/env python3

# https://github.com/Uberi/speech_recognition
# recognize_google requires internet connection

import speech_recognition as sr

def transcribe(filename):
    try:
        r = sr.Recognizer()

        lecture = sr.AudioFile("recordings/"+filename)

        with lecture as source:
            audio = r.record(source)

        text = r.recognize_google(audio)

        with open("notes/"+filename[:15]+".txt", "wb") as f:
            f.write(text)

        return filename[:15]+".txt file saved successfully."
    except OSError:
        return "Audio to text transcribe failed!"

