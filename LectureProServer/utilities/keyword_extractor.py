import nltk
from rake_nltk import Rake
from nltk.tokenize import wordpunct_tokenize


def extractPhrases(data):
    try:
        r = Rake()  # Uses stopwords for english from NLTK, and all puntuation characters.

        # keywords = r.extract_keywords_from_text(text)

        sentences = nltk.tokenize.sent_tokenize(data)

        result_list = []

        for sentence in sentences:
            word_list = [word.lower() for word in wordpunct_tokenize(sentence)]
            phrase_list = r._get_phrase_list_from_words(word_list)
            phrases = []
            for phrase in phrase_list:
                phrases.append(' '.join(map(str, phrase)))

            result_list.append([sentence, phrases[:]])

        return result_list

    except OSError:
        return "Audio to text transcribe failed!"
