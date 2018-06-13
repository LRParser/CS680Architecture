import os
import json
from functools import reduce
from operator import itemgetter
import operator
from flask_restful import Resource
from flask import current_app as app, Response

from LectureProServer.utilities.keyword_extractor import extractPhrases


class Search(Resource):
    def get(self, query):
        app.logger.info(query)

        query_keywords = [x[1] for x in extractPhrases(query)]
        query_keywords = [x for sublist in query_keywords for x in sublist]
        query_keywords = [x.lower().split() for x in query_keywords]
        query_keywords = reduce(operator.concat, query_keywords)

        results = []

        for notes_file in os.listdir("data/notes/"):
            if notes_file.endswith(".txt"):
                with open("data/notes/" + notes_file, "r") as noteFileHandler:
                    data = noteFileHandler.read()
                    note_keywords = [x[1] for x in extractPhrases(data)]
                    note_keywords = [
                        x for sublist in note_keywords for x in sublist]
                    note_keywords = [x.lower() for x in note_keywords]

                file_hits = 0
                for query_keyword in query_keywords:
                    for note_keyword in note_keywords:
                        if query_keyword in note_keyword:
                            file_hits += 1

                if file_hits > 0:
                    results.append([notes_file, file_hits])

        results = sorted(results, key=itemgetter(1), reverse=True)
        ordered_files = [x[0] for x in results]

        print(ordered_files)
        return Response(json.dumps(ordered_files),  mimetype='application/json')
