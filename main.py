from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    get = request.args
    if get["name"].lower() == "mikee":
        return "Hello babe"


app.run(host='0.0.0.0', port=81)
