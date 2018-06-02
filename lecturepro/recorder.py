#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import datetime


def record():
# obtain audio from the microphone
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)


        timestamp = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')).split('.')[0]
        # write audio to a WAV file
        with open("recordings/"+timestamp+".wav", "wb") as f:
            f.write(audio.get_wav_data())

        return "Audio recording saved successfully."
    except OSError:
        return "Audio recording failed."