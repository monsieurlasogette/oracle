
#

<div style="display:block;text-align:left"><a href="https://github.com/Eccentrici/" imageanchor="1"><img align="left" src="https://c.tenor.com/WIqvnT_7Vj8AAAAi/terry-a-davis-terry-davis.gif" border="" style="width:200px;"></a></div>
    
    
## GodspeakAPI
<p>A simple API for generating random words ("godspeaks"), inspired by the works of Terrence Andrew Davis (Rest In Peace, King).</p>

### Installation  
```sh
git clone https://github.com/eccentrici/godspeakapi.git
cd godspeakapi
pip install -r r.txt
python main.py
```
### Usage
<p>If you don't wish to host the GodspeakAPI yourself; I offer my own public 
available API at <a href="http://i386.tk/">i386.tk</a>. I will be using that 
website below, if you are self hosting; use your loopback or your fowarded host.</p>
 
```sh
curl -L -X GET -H 'Content-Type: application/json' http://i386.tk/get\?num\=1 
```

If you wish to use the Vocab.DD vocabulary:

```sh
curl -L -X GET -H 'Content-Type: application/json' http://i386.tk/get\?num\=5&dict=vocab
```
If you wish to extract only the Godspeak data you can do so using jq:
```sh
curl -s -L -X GET -H 'Content-Type: application/json' http://i386.tk/get\?num\=1 | jq '.Godspeak'
```

### Example
Usage within the Python Interpreter:

```python
>>> import requests
>>> response = requests.get('http://i386.tk/get?num=1')
>>> print(response.json()['Godspeak'])
don't_even_think_about_it
```
### Credit
Thank you [xslendix](https://github.com/xslendix), for making some changes to my code. You can view their own take, with even more endpoints at https://git.kiwifarms.net/slendi/TempleAPI
