# save this as app.py
from flask import Flask
from flask import render_template
from flask import json
from flask import request
from flask import session
import base64

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
    return render_template("rules_add.html")

@app.route("/alias")
def alias():
    return render_template("alias.html")

'''
///////////////
// Function //
/////////////
'''

###########################
## Check if user in file ##
##  Return log + passwd  ##
###########################
def check_authen(login, passwd):
    with open(log.txt) as temp_f:
        datafile = temp_f.readlines()
    for lines in datafile:
        if login in line:
            return line
    return False

############################
## Check if session exist ##
############################

def chek_user():
    if 'login' in session:
        return True
    else:
        return False

###########################
## Add user if not exist ##
###########################

def add_user(login, passwd):
    fichier = open("log.txt", "a")
    passwd = base64.b64encode(passwd.encode())
    fichier.write(str(login) + ':' + str(passwd))
    fichier.close()