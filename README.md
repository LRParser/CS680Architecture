# CS680Architecture

CS680Architecture

## Demo

A demo is available at:

https://youtu.be/-_Mgz821fqw

## Installation

Copy the entire CS680Architecture folder to both client and server.

Ensure that Python 3.6 or 2.7 is installed. Any OS supporting Python should be fine. Ideally Python 3.6 should be used. The pip utility should be available. Install the below packages when inside the CS680Architecture folder on both client and server via the following command:

pip install flask flask-restful speechrecognition rake-nltk



## Running the client

Open a terminal and do:

```
cd LectureProClient
export FLASK_APP=client.py
export FLASK_ENV=development
flask run
```

### Running the server

Open another terminal and do:

```
cd LectureProServer
export FLASK_APP=server.py
export FLASK_ENV=development
flask run -p 8080
```

### Running as Docker

1.  Install Docker (https://docs.docker.com/install/#desktop)
2.  `cd LectureProServer`
3.  `docker build -t lecturepro-server:latest .`
4.  `docker run -d -p 8080:5000 lecturepro-server`

Server will be running in port 8080.
