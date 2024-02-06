from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


@app.route("/username/<username>")
def about(username):
    return f"<h1> Hello {username}! </h1>"


@app.route("/login")
def login():
    return render_template("index.html")
