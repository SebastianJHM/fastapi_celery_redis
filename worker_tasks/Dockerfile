FROM python:3.8

#Set the working directory
WORKDIR /

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y --no-install-recommends python3-pip python3-dev

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

#COPY app.py /app.py
ADD . /worker_tasks
WORKDIR /worker_tasks

ENTRYPOINT celery -A tasks worker --loglevel=info