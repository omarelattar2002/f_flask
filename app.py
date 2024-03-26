from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    name = 'Omar'
    age = 22
    return f'Hello ' + name + ' who is ' + str(age)