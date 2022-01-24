#!/usr/bin/env python3
# Imports

import os
import random
import time
import json

import urllib.request

from flask import *
from flask import render_template

app = Flask(__name__, template_folder='./template', static_folder='./static')
unixTime = round(time.time() * 1000)

@app.route('/get/', methods=['GET'])
def requestRoute():
    try:
        query = int(request.args.get('num'))

        dictionary = str(request.args.get('dict'))
        if dictionary.startswith('vocab'):
            dictionary = 'Vocab.DD'
        else:
            dictionary = 'Happy.TXT'

        file = open(dictionary, "r")
        data = file.read()
        vocabList = data.split("\n")
        file.close()

        numbers = [random.randint(0, len(vocabList)-1) for i in range(query)]
        godswords = []

        for i in numbers:
            godswords.append(vocabList[i])

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
    port = 80
    if os.geteuid() != 0:
        port = 8080

    app.run(host="0.0.0.0", port=port)

