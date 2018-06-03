#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import datetime


def voicerecord():
    # obtain audio from the microphone
    try:
        r = sr.Recognizer()
        r.pause_threshold = 1
        r.dynamic_energy_threshold = True
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        timestamp = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')).split('.')[0]
        # write audio to a WAV file
        with open("RecorderHandler/recordings/"+timestamp+".wav", "wb") as f:
            f.write(audio.get_wav_data())
            file = timestamp+".wav"

        return file
    except OSError:
        return "Audio recording failed."