FROM java:8

MAINTAINER Casey Hilland <casey dot hilland at gmail dot com>

RUN apt-get update && apt-get install -y git build-essential wget unzip python-setuptools

RUN easy_install pip
RUN pip install --upgrade pip
ADD . /src
RUN pip install -r /src/requirements.txt

RUN mkdir /home/ubuntu

RUN cd /home/ubuntu/; wget http://nlp.stanford.edu/software/stanford-corenlp-full-2015-04-20.zip
RUN cd /home/ubuntu; unzip stanford-corenlp-full-2015-04-20.zip
RUN cd /home/ubuntu/stanford-corenlp-full-2015-04-20; wget http://nlp.stanford.edu/software/stanford-srparser-2014-10-23-models.jar

WORKDIR /src

EXPOSE 5000

CMD ["python", "app.py"]
