# https://github.com/Uberi/speech_recognition
# recognize_google requires internet connection

import speech_recognition as sr
from flask import current_app as app


def translate(file):
    try:
        r = sr.Recognizer()

        lecture = sr.AudioFile(file)

        with lecture as source:
            audio = r.record(source)

        text = r.recognize_google(audio)
        app.logger.info(text)
        app.logger.info(file[:15]+".txt file saved successfully.")
        return text
    except OSError as err:
        app.logger.info("OS error: {0}".format(err))
        return "Audio to text transcribe failed!"
