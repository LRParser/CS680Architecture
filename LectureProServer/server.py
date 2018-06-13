from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import logging
from logging.handlers import RotatingFileHandler

from LectureProServer.resources.helloworld import HelloWorld
from LectureProServer.resources.lecture import Lecture
from LectureProServer.resources.keyword import Keyword
from LectureProServer.resources.search import Search

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(Lecture, '/Lecture')
api.add_resource(Keyword, '/Keyword/<string:file>')
api.add_resource(Search, "/Search/<string:query>")


if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True, host='0.0.0.0',port=8080)
