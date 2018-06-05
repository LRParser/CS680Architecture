# CS680Architecture

CS680Architecture

## Installation

pip install flask

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
