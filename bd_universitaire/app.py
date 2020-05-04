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
from flask import Flask, render_template
import pymysql
import pymysql.cursors


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='Reussite2019',
                       db='bd_universitaire' )

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    idul = '"'+request.form.get('idul')+'"'
    passe = request.form.get('motDePasse')
    cmd = 'SELECT motDePasse FROM Etudiant WHERE idul='+idul+';'
    cur = conn.cursor()
    cur.execute(cmd)
    passeVrai = cur.fetchone()

    if (passeVrai != None) and (passe == passeVrai[0]):
        cmd = 'SELECT * FROM Etudiant WHERE idul=' + idul + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        info = cur.fetchone()

        global ProfileUtilisateur
        ProfileUtilisateur["idul"] = idulProfileUtilisateur
        ProfileUtilisateur["nom"] = info[2]
        ProfileUtilisateur["avatar"] = info[3]
        return render_template('bienvenu.html', profile=ProfileUtilisateur)
        return render_template('index.html', message="Informations invalides!")

if __name__ == "__main__":
    app.run()