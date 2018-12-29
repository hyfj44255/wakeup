FROM python:3.6-slim

RUN apt-get update -y  && apt-get install -y procps

WORKDIR /usr/src/app/

ADD double /usr/src/app/double

RUN pip install -r /usr/src/app/double/requirements.txt

CMD ["/usr/src/app/double/start.sh",">","/usr/src/app/double/allLog.txt"]
