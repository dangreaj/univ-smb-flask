# save this as app.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/start")
def start():
    return render_template("index.html")

@app.route("/rules_nat")
def rules_nat():
    return render_template("nat.html")

@app.route("/rules_nat_add")
def rules_nat_add():
    return render_template("regle.html")

@app.route("/alias")
def alias():
    return render_template("alias.html")
