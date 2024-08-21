from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/test")
def hello_test():
    return jsonify({'status': 'test', 'data': [1,2,3]})
