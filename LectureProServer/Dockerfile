# Build Docker Image
# docker build -t lecturepro-server:latest .

# Run Docker Image
# docker run -d -p 8080:5000 lecturepro-server

# docker rm -f server && docker build -t lecturepro-server:latest . && docker run --name server -d -p 8080:5000 lecturepro-server && docker logs -f server

FROM ubuntu:xenial

MAINTAINER Alex Raju "alexforever86@gmail.com"

ENV FLASK_APP server.py
ENV FLASK_ENV development
ENV LC_ALL C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update -y
RUN apt-get install -y \
    python3-pip \
    python3-dev  \
    build-essential \
    portaudio19-dev
RUN pip3 install --upgrade pip

WORKDIR /LectureProServer
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . /LectureProServer

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]