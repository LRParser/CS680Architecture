#!/usr/bin/env python3

import recorder


def run():
    print "Welcome to LecturePro! Would you like to record a new lecture(n), or [future options here]"
    action = raw_input()

    if action == "n":
        recorderdelegator = recorder
        record = recorderdelegator.record()
        print record
    else:
        print "Invalid Option!"



run()