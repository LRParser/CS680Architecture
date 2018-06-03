#!/usr/bin/env python3

import sys
from RecorderHandler import recorder_handler
sys.path.append('../')
import LectureProServer.server

def run():
    print "Welcome to LecturePro! Would you like to record a new lecture(n), or [future options here]"
    action = raw_input()

    if action == "n":
        # Create new RecorderDelegator to handle the audio recording
        recorder_delegator = recorder_handler
        file = recorder_delegator.voicerecord()

        # call server with file
        server = LectureProServer.server
        translation = server.translate(file)
        print(translation)

        extraction = server.extractphrases(file)
        print(extraction)

    else:
        print("Invalid Option!")


run()