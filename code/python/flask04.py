from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/help')
def help():
    return 'Textes for help!'

@app.route("/calc",methods=['GET'])
def calc():
    if request.method == "GET":
        if request.args.get('a') == None:
            a = 0
        else:
            a = int(request.args.get('a'))
        if request.args.get('b') == None:
            b = 0
        else:
            b = int(request.args.get('b'))
        c = a + b

    return f"{a}+{b}={c}"
