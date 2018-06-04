import os
from flask import Flask, flash, request, redirect, url_for
from flask_restful import Resource, reqparse
from flask import current_app as app

from LectureProServer.utilities.recorder_handler import translate

parser = reqparse.RequestParser()


class Lecture(Resource):
    def get(self):
        return "Hello world"

    def post(self):
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.urls)
            return "no file"
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "empty file"
        filename = file.filename
        saved_as = os.path.join('data/recordings', filename)
        app.logger.info(saved_as)
        file.save(saved_as)

        # Create new TranslateDelegator to handle voice to text translation
        # translate_delegator = recorder_handler
        transcribe = translate("data/recordings/"+filename)

        with open("data/notes/" + filename[:15] + ".txt", "w") as f:
            f.write(transcribe)

        return transcribe
