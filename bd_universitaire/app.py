'''
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pr@j?vision100%@$!'
app.config['MYSQL_DB'] = 'bd_universitaire'

mysql = MySQL(app)
@app.route('/bd_universitaire/', methods=['GET', 'POST'])
def login():
    return render_template('../mon site web/Sanstitre-2.html', msg='')
@app.route("/")
def chart():
    return render_template('../Site web/Connexion - Université Laval.html')

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=5001)

if __name__ == "__main__":
    app.run()

'''
from flask import Flask , render_template , request
import pymysql
import pymysql.cursors
import re
from password import makehash

conn = pymysql.connect(host='localhost',
                           user='root',
                           password='Reussite2019',
                           db='bd_universitaire')



app = Flask(__name__)
ProfileUtilisateur =  {}
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def login():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='Reussite2019',
                           db='bd_universitaire')
    if request.method == 'GET':
        pass
    if request.method == 'POST':

        idul = '"'+request.form.get('username')+'"'
        passe = makehash(request.form.get('password'))
        cmd = 'SELECT motDePasse FROM Etudiant WHERE idul='+idul+';'
        cur = conn.cursor()
        cur.execute(cmd)
        passeVrai = cur.fetchone()
        if (passeVrai != None) and (passe == passeVrai[0]):
            cmd = 'SELECT * FROM Etudiant WHERE idul='+idul+';'
            cur = conn.cursor()
            cur.execute(cmd)
            info = cur.fetchone()


            return render_template('Sanstitre-2.html')
        return render_template('index.html', msg="Informations invalides!")

@app.route('//register', methods=['GET', 'POST'])
def register():

    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form :
        # Create variables for easy access
        idul = "'" + request.form.get('username') + "'"
        passe = "'" + makehash(request.form.get('password')) + "'"
        password = request.form.get('password')
        credit = request.form.get('credit')
        nom = "'" + request.form.get('nom') + "'"
        sigleProgramme = "'" + request.form.get('sigleProgramme') + "'"
        motivation = 5

        cmd = 'SELECT * FROM Etudiant WHERE idul='+ idul +';'
        cur = conn.cursor()
        cur.execute(cmd)
        etudiant = cur.fetchone()
        # If account exists show error and validation checks
        if etudiant:
            msg = 'Account already exists!'

        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cmd='INSERT INTO Etudiant VALUES '+'('+ idul +','+ nom +','+ passe +','+ str(motivation) +',' +str(credit)+ ',' + sigleProgramme+ ')'+ ';'
            cur = conn.cursor()
            cur.execute(cmd)
            print (cmd)
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


if __name__ == "__main__":
    app.run()