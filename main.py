# Imports

import time, json, urllib.request
from flask import *
app = Flask(__name__)
unixTime = round(time.time() * 1000)
@app.route('/request/', methods=['GET'])
def requestRoute():
    try:
        query = str(request.args.get('num'))
        output = urllib.request.urlopen(f"https://www.random.org/integers/?num={query}&min=0&max=712&col=1&base=10&format=plain&rnd=new")
        numbers = []
        for word in output.read().split():
            if word.isdigit():
                numbers.append(int(word))

        file = open("Happy.TXT", "r")
        data = file.read()
        vocabList = data.split("\n")
        file.close() 
        godswords = [] 
        for i in range(len(numbers)):
            godswords.append(vocabList[numbers[i]])

        speaketh = ' '.join(godswords)
        data = {"Status": 200, "Count": f"{query}", "Godspeak": f"{speaketh}", "Time": f"{unixTime}"}
    
    except:
        data = {"Status: 400", "Time": f"{unixTime}"}
    return json.dumps(data)

if __name__ == "__main__":
    app.run(port=767) # Port.
