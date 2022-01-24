#!/usr/bin/env python3
# Imports

import time
import json
import random

import urllib.request

from flask import *
from flask import render_template

app = Flask(__name__, template_folder='./template', static_folder='./static')
unixTime = round(time.time() * 1000)

@app.route('/get/', methods=['GET'])
def requestRoute():
    try:
        query = int(request.args.get('num'))
        numbers = [random.randint(0, 712) for i in range(query)]

        dictionary = str(request.args.get('dict'))
        if dictionary.startswith('vocab'):
            dictionary = 'Vocab.DD'
        else:
            dictionary = 'Happy.TXT'

        file = open(dictionary, "r")
        data = file.read()
        vocabList = data.split("\n")
        file.close()
        godswords = []
        for i in range(len(numbers)):
            godswords.append(vocabList[numbers[i]])

        speaketh = ' '.join(godswords)
        data = {"Count": f"{query}", "Godspeak": f"{speaketh}", "Time": f"{unixTime}"}
        s = 200

    except:
        s = 400
        data = {"Time": f"{unixTime}"}
    r = make_response(data)
    r.minetype = 'application/json'
    return r

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80) # Port.

