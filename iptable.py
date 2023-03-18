# save this as app.py
from flask import Flask
from flask import render_template
from flask import json
from flask import request
from flask import session
import base64


app = Flask(__name__)
app.debug = True
app.secret_key = 'any'

@app.route("/")
def hello():
    if user_registered():
        return render_template("index.html")
    else:
        return render_template("connexion.html")

@app.route("/start")
def index():
    if user_registered():
        return render_template("index.html")
    else:
        return render_template("connexion.html")

@app_route("/alias"):
def alias():
    if user_registered():
        return render_template("alias.html")
    else:
        return render_template("connexion.html")

@app.route("/rules_nat_add")
def rules_add():
    if user_registered():
        return render_template("rules_add.html")
    else:
        return render_template("connexion.html")

@app.rotue("/rules_filters")
def rules_filetrs():
    if user_registered():
        return render_template("nat.html")
    else:
        return render_template("connexion.html")

@app.route("/connect", methods=['POST'])
def connect():
    result = request.form
    login = result['login']
    passwd = result['password']
    
    if check_connect(login, passwd):
        return render_template("index.html")
    else:
        return render_template("connexion.html")

@app.route("/disconnect")
def disconnect():
    session.clear()
    return index()

###############################
## Declaration des fonctions ##
###############################

def user_connect(login, passwd):
    passwd = base64.b64encode(passwd, encode())
    res = in_folder(login) # Get line if in_foldef , False if not in folder
    print(res)
    if res:
        print(res)
        if passwd:
            session['login'] =login
            print('session', session['login'])
            return True
        
        else:
            return False
    else:
        return False
    
# Check if user in folder
# return his log + pw 
def in_folder(login):
    with open('log.txt') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if login in line:
            return line
    return False

#check if session exist
def user_registered():
    if 'login' in session:
        return True
    else:
        return False

# Add user
def add_user_files(login,passwd):
    fichier = open('login.txt','a')
    passwd = base64.b64encode(passwd.encode())
    ficheir.write(str(login) + ':' + str(passwd))
    ficher.close()