#!/usr/bin/env python3

import nltk
from rake_nltk import Rake
from nltk.tokenize import wordpunct_tokenize


def extractPhrases(file):
    try:
        with open("../RecorderHandler/notes/"+file[:15]+".txt", "r") as f:
            data = f.read()

        r = Rake()  # Uses stopwords for english from NLTK, and all puntuation characters.

        # keywords = r.extract_keywords_from_text(text)

        sentences = nltk.tokenize.sent_tokenize(data)

        for sentence in sentences:
            word_list = [word.lower() for word in wordpunct_tokenize(sentence)]
            phrase_list = r._get_phrase_list_from_words(word_list)
            phrases = []
            for phrase in phrase_list:
                phrases.append(' '.join(map(str, phrase)))

            note = "Full sentence: " + sentence + "\n" + "\n" + "Key phrases: " + str(phrases)

            with open("../KeywordExtractor/notes/"+file[:15]+"_notes.txt", "wb") as f:
                f.write(note)

            return file[:15]+"_notes.txt file saved successfully."
    except OSError:
        return "Audio to text transcribe failed!"
