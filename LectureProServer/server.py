#!/usr/bin/env python3


from LectureProServer.RecorderHandler import recorder_handler
from LectureProServer.KeywordExtractor import keyword_extractor


def translate(file):
    # Create new TranslateDelegator to handle voice to text translation
    translate_delegator = recorder_handler
    transcribe = translate_delegator.translate(file)

    return transcribe


def extractphrases(file):
    # Create new ExtractorDelegator to handle keyword extractor
    extractor_delegator = keyword_extractor
    extract = extractor_delegator.extractPhrases(file)

    return extract
