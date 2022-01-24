
#

<div style="display:block;text-align:left"><a href="https://github.com/Eccentrici/" imageanchor="1"><img align="left" src="https://c.tenor.com/WIqvnT_7Vj8AAAAi/terry-a-davis-terry-davis.gif" border="" style="width:155px;">

### GodspeakAPI
A simple API for generating random words ("godspeaks"), inspired by the works of Terrence Andrew Davis (Rest In Peace, King).

### Installation
<i>This section covers how to install GodspeakAPI Locally, otherwise check [Usage](###usage)</i>

    git clone https://github.com/eccentrici/godspeakapi.git
    cd godspeakapi
    pip install -r r.txt
    python main.py
 ### Usage
 If you don't wish to host the GodspeakAPI yourself; I offer my own public available API at http://i386.tk/. I will be using that website below, if you are self hosting; use your loopback or your fowarded host.
 

    curl -L -X GET -H 'Content-Type: application/json' http://i386.tk/get\?num\=1 

Currently the "Happy.TXT" file, which was used by Terry in his Happy.sh program, is used for Godspeak. Additional support for the "Vocab.DD" file - that features a far greater amount of words - will be added soon.
### Example
Usage within the Python Interpreter:
```python
>>> import requests
>>> response = requests.get('http://i386.tk/get?num=1')
>>> print(response.json()['Godspeak'])
don't_even_think_about_it
```
