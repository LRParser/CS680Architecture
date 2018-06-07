from flask_restful import Resource
from flask import current_app as app

from LectureProServer.utilities.keyword_extractor import extractPhrases


class Keyword(Resource):
    def get(self, file):
        app.logger.info(file)
        try:
            with open("data/notes/" + file[:15] + ".txt", "r") as noteFileHandler:
                data = noteFileHandler.read()
                # Create new ExtractorDelegator to handle keyword extractor
                # extractor_delegator = keyword_extractor
                keyword = extractPhrases(data)

                with open("data/keywords/" + file[:15] + "_notes.txt", "w") as keywordFileHandler:
                    keywordFileHandler.write("Full sentence:{}\n\nKey phrases{}".format(keyword[0], keyword[1]))

                app.logger.info(file[:15] + "_notes.txt file saved successfully.")
                return keyword
        except OSError as err:
            app.logger.info("OS error: {0}".format(err))
            return "Audio to text transcribe failed!", 422

