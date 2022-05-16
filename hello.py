from flask import Flask
from flask import render_template # calling html files in templates folder

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html") # calling html files in templates folder

@app.route("/world/<country>")
def world(country):
    return f"<h1>Hello, {country}!</h1>"

sport = [
    "Baseball",
    "Football",
    "Basketball",
    "Tennis",
    "Table tennis",
    "Cricket",
    "American football",
    "Rugby"
]

@app.route("/sports/")
def sports():
    return render_template("sports.html", sport=sport)



