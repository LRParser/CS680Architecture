import os
from functools import reduce
from operator import itemgetter
import operator
from flask_restful import Resource
from flask import current_app as app

from LectureProServer.utilities.keyword_extractor import extractPhrases

''
class Search(Resource):
    def get(self, query):
        app.logger.info(query)

        query_keywords = extractPhrases(query)[1]
        query_keywords = [x.lower().split() for x in query_keywords]
        query_keywords = reduce(operator.concat, query_keywords)

        results = []

        print(query_keywords)

        for notes_file in os.listdir("data/notes/"):
            if notes_file.endswith(".txt"):
                print(notes_file)
                with open("data/notes/" + notes_file, "r") as noteFileHandler:
                    data = noteFileHandler.read()
                    note_keywords = extractPhrases(data)[1]
                    print(note_keywords)
                    note_keywords = [x.lower() for x in note_keywords]

                file_hits=0
                for query_keyword in query_keywords:
                    for note_keyword in note_keywords:
                        print(query_keyword)
                        if query_keyword in note_keyword:
                            print("hit")
                            file_hits += 1

                if file_hits > 0:
                    results.append([notes_file, file_hits])



        results = sorted(results, key=itemgetter(1), reverse=True)
        ordered_files = [x[0] for x in results]

        print(ordered_files)
        return ordered_files