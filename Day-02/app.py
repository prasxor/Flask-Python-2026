from flask import Flask,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if response
    return "this is home page"

@app.route("/about")
def about():
    return "this is about section"

