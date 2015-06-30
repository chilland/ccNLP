# ccNLP

Containerized CoreNLP

ccNLP serves up Brendan O'Connor's Stanford CoreNLP
[wrapper](https://github.com/brendano/stanford_corenlp_pywrapper) as an API.
Its a wrapper for a wrapper...

There are probably a number of ways this can be done much better, particularly
by someone with some Java skills. However I have yet to come across a fast
implementation of [Stanford
CoreNLP](http://nlp.stanford.edu/software/corenlp.shtml) as a RESTful API, so
in the meantime this will do. Pull requests welcome.

ccNLP runs as a Flask-RESTful service on port `5000`. You can can configure the
parser just as you would with the normal wrapper in
`resources/stanford_config.ini`. Set the path to the jars in
`resources/config.ini`. 

Its also Dockerized, which will hopefully make it easier to run, but it should
also work natively.

Installation
-------------

1. Make sure you have [docker](https://www.docker.com/) installed
2. Build the image: `sudo docker build -t ccnlp .`
3. Startup a container: `sudo docker run -d -p 5000:5000 ccnlp`

Usage
------

###Python

```
import json
import requests

headers = {'Content-Type': 'application/json'}
data = {'text': 'Stanford CoreNLP provides a set of natural language analysis tools which can take raw text input and give the base forms of words, their parts of speech, whether they are names of companies, people, etc., normalize dates, times, and numeric quantities, and mark up the structure of sentences in terms of phrases and word dependencies, indicate which noun phrases refer to the same entities, indicate sentiment, etc.'}
data = json.dumps(data)
r = requests.post('http://localhost:5000/process', data=data,
headers=headers)
r.json()
```
