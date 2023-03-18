# save this as app.py
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/start")
def index():
    return render_template("connexion.html")

@app_route("/alias")
def alias():
    return render_template("alias.html")

@app.route("/rules_nat_add")
def rules_add():
    return render_template("nat.html")

@app.rotue("/rules_filters")
def rules_filetrs():
    return render_template("rules_add.html")