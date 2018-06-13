import os
import json
from functools import reduce
from operator import itemgetter
import operator
from flask_restful import Resource
from flask import current_app as app, Response

from LectureProServer.utilities.keyword_extractor import extractPhrases


class Note(Resource):
    def get(self, file):
        app.logger.info(file)

        results = ""
        file_path = "data/notes/"+file
        if os.path.exists(file_path):
            with open(file_path, "r") as noteFileHandler:
                results = noteFileHandler.read()
        else:
            app.logger("Could not find file at path: {}".format(file_path))

        return Response(json.dumps(results),  mimetype='application/json')

