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
    if check_user():
        return render_template("index.html")
    else:
        return render_template("connexion.html")

@app.route("/start")
def start():
    if check_user():
        return render_template("index.html")
    else:
        return render_template("connexion.html")

@app.route("/rules_nat")
def rules_nat():
    if check_user():
        with open("static/nat.json") as nat:
            data = json.load(nat)
        return render_template("nat.html", nat=data)
    else:
        return render_template("connexion.html")

@app.route("/rules_nat_add")
def rules_nat_add():
    if check_user():
        return render_template("rules_add.html")
    else:
        return render_template("connexion.html")

@app.route("/alias")
def alias():
    if check_user():
        with open("static/alias.json") as alias:
            data = json.load(alias)
        return render_template("alias.html", alias=data)
    else:
        return render_template("connexion.html")

@app.route("/connect", methods=['POST'])
def connexion():
    res = request.form
    login = res['login']
    passwd = res['passwd']
    if check_authen(login, passwd):
        return render_template("index.html")
    else:
        return render_template("connexion.html")

@app.route ("/disconnect")
def disconnect():
    session.clear()
    return start()


'''
///////////////
// Function //
/////////////
'''
def check_authen(login, passwd):
    passwd = base64.b64encode(passwd.encode())
    res = in_folder(login) # Check if this account is in folder , if not return False
    print(res)
    if res:
        print(res)
        if passwd:
            session['login'] = login
            print (session, session['login'])
            return True
        else:
            return False
    else:
        return False

###########################
## Check if user in file ##
##  Return log + passwd  ##
###########################
def in_folder(login):
    with open('log.txt') as temp_f:
        datafile = temp_f.readlines()
    for lines in datafile:
        if login in lines:
            return lines
    return False

############################
## Check if session exist ##
############################

def check_user():
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