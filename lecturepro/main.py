#!/usr/bin/env python3

import recorder
import transcriber


def run():
    print "Welcome to LecturePro! Would you like to record a new lecture(n), or [future options here]"
    action = raw_input()

    if action == "n":
        # Create new RecorderDelegator to handle the audio recording
        recorderdelegator = recorder
        record = recorderdelegator.record()
        print record

        filename = record[:19]
        # Create new TranscribeDelegator to handle voice to text translation
        transcriberdelegator = transcriber
        transcribe = transcriberdelegator.transcribe(filename)
        print transcribe

    else:
        print "Invalid Option!"


run()