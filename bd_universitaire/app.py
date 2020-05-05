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
from flask import Flask , render_template , request, Markup
import pymysql
import pymysql.cursors
import re
from password import makehash
from moyenne import moyenne_ponderee
from moyenne import atteindre

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [1,2,3,4,5]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]



conn = pymysql.connect(host='localhost',
                           user='root',
                           password='theonina',
                           db='bd_universitaire')


app = Flask(__name__)
ProfileUtilisateur =  {}
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def login():

    if request.method == 'GET':
        pass
    if request.method == 'POST':
        global idul
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
        global motivation
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
            conn.commit()
            print (cmd)
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

@app.route("//Cours/Acceuil")
def Acceuil():
    return render_template('Sanstitre-2.html')

@app.route("//Profile/Acceuil")
def Acceuil1():
    return render_template('Sanstitre-2.html')

@app.route("//Cours")
def Cours():
    cmd = 'SELECT c.nom FROM Cours c, Suivre s WHERE s.idul=' + idul + 'and c.sigleCours= s.sigleCours ;'
    cur = conn.cursor()
    cur.execute(cmd)

    info = cur.fetchall()
    global info1,info2,info3,info3,info4,info5,info5, info6
    info1 = str(info[0])[2:-3]
    info2 = str(info[1])[2:-3]
    info3 = str(info[2])[2:-3]
    info4 = str(info[3])[2:-3]
    info5 = str(info[4])[2:-3]
    info6 = str(info[5])[2:-3]




    print(info)
    return render_template('Sanstitre-3.html', cours01=info1,cours02=info2,cours03=info3,cours04=info4,cours05=info5,cours06=info6)
@app.route("//Cours/Calul")
def Cours1():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" +info1 +"'"+ ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' +"'" +sigleCours +"'"+ 'and n.idul = '+idul+';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    nbr_exam =[]
    for i in range((len(note))):
        note1.append(str(note[i])[1:-2])
    print(note)

    for i in range((len(note))):
        nbr_exam.append("NOTE"+str(i+1))







    bar_labels=labels
    bar_values=values
    return render_template('graphique.html', max=100, labels=nbr_exam, values=note1,title=info1)
@app.route("//Cours/Calul2")
def Cours2():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" +info2+"'"+ ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' +"'" +sigleCours +"'"+ 'and n.idul = '+idul+';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    nbr_exam =[]
    for i in range((len(note))):
        note1.append(str(note[i])[1:-2])
    print(note)

    for i in range((len(note))):
        nbr_exam.append("NOTE"+str(i+1))



    bar_labels=labels
    bar_values=values
    return render_template('graphique.html', max=100, labels=nbr_exam, values=note1, title=info2)

@app.route("//Cours/Calul3")
def Cours3():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" +info3+"'"+ ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' +"'" +sigleCours +"'"+ 'and n.idul = '+idul+';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    nbr_exam =[]
    for i in range((len(note))):
        note1.append(str(note[i])[1:-2])
    print(note)

    for i in range((len(note))):
        nbr_exam.append("NOTE"+str(i+1))







    bar_labels=labels
    bar_values=values
    return render_template('graphique.html', max=100, labels=nbr_exam, values=note1, title=info3)



@app.route("//Cours/Calul4")
def Cours4():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" +info4+"'"+ ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' +"'" +sigleCours +"'"+ 'and n.idul = '+idul+';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    nbr_exam =[]
    for i in range((len(note))):
        note1.append(str(note[i])[1:-2])
    print(note)

    for i in range((len(note))):
        nbr_exam.append("NOTE"+str(i+1))







    bar_labels=labels
    bar_values=values
    return render_template('graphique.html', max=100, labels=nbr_exam, values=note1, title=info4)


@app.route("//Cours/Calul5")
def Cours5():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" +info5+"'"+ ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' +"'" +sigleCours +"'"+ 'and n.idul = '+idul+';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    nbr_exam =[]
    for i in range((len(note))):
        note1.append(str(note[i])[1:-2])
    print(note)

    for i in range((len(note))):
        nbr_exam.append("NOTE"+str(i+1))







    bar_labels=labels
    bar_values=values
    return render_template('graphique.html', max=100, labels=nbr_exam, values=note1, title=info5)
@app.route("//Cours/Calul6")
def Cours6():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" +info5+"'"+ ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' +"'" +sigleCours +"'"+ 'and n.idul = '+idul+';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    nbr_exam =[]
    for i in range((len(note))):
        note1.append(str(note[i])[1:-2])
    print(note)

    for i in range((len(note))):
        nbr_exam.append("NOTE"+str(i+1))







    bar_labels=labels
    bar_values=values
    return render_template('graphique.html', max=100, labels=nbr_exam, values=note1, title=info6)

@app.route("//Cours/Profile")
def Profile():

    cmd = 'SELECT p.nom FROM Programme p, Etudiant e WHERE e.idul=' + idul +  'and e.sigleProgramme = p.sigleProgramme;'
    cur = conn.cursor()
    cur.execute(cmd)
    nomProg = str(cur.fetchone())[2:-3]
    motivation = 5

    return render_template('profile.html', prog=nomProg, motiv=motivation)

@app.route("//Prevision")
def Prevision():
    cmd = 'SELECT c.nom FROM Cours c, Suivre s WHERE s.idul=' + idul + 'and c.sigleCours= s.sigleCours ;'
    cur = conn.cursor()
    cur.execute(cmd)

    info = cur.fetchall()
    global info1,info2,info3,info3,info4,info5,info5
    info1 = str(info[0])[2:-3]
    info2 = str(info[1])[2:-3]
    info3 = str(info[2])[2:-3]
    info4 = str(info[3])[2:-3]
    info5 = str(info[4])[2:-3]
    info6 = str(info[5])[2:-3]




    print(info)
    return render_template('listeCours.html', cours01=info1,cours02=info2,cours03=info3,cours04=info4,cours05=info5,cours06=info6)

@app.route("//Prevision/Calcul1")
def Calcul1():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" +info1 +"'"+ ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' +"'" +sigleCours +"'"+ 'and n.idul = '+idul+';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    totaux = []
    nbr_exam = []
    for i in range((len(note))):
        totaux.append(str(100))
        note1.append(str(note[i])[1:-2])
    print(note)
    cmd = 'SELECT n.ponderation FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    ponderation = cur.fetchall()
    ponderation1 = []
    nbr_exam = []
    for i in range((len(ponderation))):
        ponderation1.append(str(ponderation[i])[1:-2])
    print(ponderation1)
    for i in range((len(ponderation))):
        nbr_exam.append("NOTE"+str(i+1))







    bar_labels=labels
    bar_values=values
    return render_template('prevision.html', max=100, labels=nbr_exam, values=note1,title=info1)
@app.route("//Prevision/Calcul2")
def Calcul2():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" + info2 + "'" + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    totaux = []
    nbr_exam = []
    for i in range((len(note))):
        totaux.append(str(100))
        note1.append(str(note[i])[1:-2])
    print(note)
    cmd = 'SELECT n.ponderation FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    ponderation = cur.fetchall()
    ponderation1 = []
    nbr_exam = []
    for i in range((len(ponderation))):
        ponderation1.append(str(ponderation[i])[1:-2])
    print(ponderation1)
    for i in range((len(ponderation))):
        nbr_exam.append("NOTE" + str(i + 1))

    bar_labels = labels
    bar_values = values
    return render_template('prevision.html', max=100, labels=nbr_exam, values=note1,title=info1)

@app.route("//Prevision/Calcul3")
def Calcul3():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" + info3 + "'" + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    totaux = []
    nbr_exam = []
    for i in range((len(note))):
        totaux.append(str(100))
        note1.append(str(note[i])[1:-2])
    print(note)
    cmd = 'SELECT n.ponderation FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    ponderation = cur.fetchall()
    ponderation1 = []
    nbr_exam = []
    for i in range((len(ponderation))):
        ponderation1.append(str(ponderation[i])[1:-2])
    print(ponderation1)
    for i in range((len(ponderation))):
        nbr_exam.append("NOTE" + str(i + 1))

    bar_labels = labels
    bar_values = values
    return render_template('prevision.html', max=100, labels=nbr_exam, values=note1,title=info1)

@app.route("//Prevision/Calcul4")
def Calcul4():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" + info4 + "'" + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    totaux = []
    nbr_exam = []
    for i in range((len(note))):
        totaux.append(str(100))
        note1.append(str(note[i])[1:-2])
    print(note)
    cmd = 'SELECT n.ponderation FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    ponderation = cur.fetchall()
    ponderation1 = []
    nbr_exam = []
    for i in range((len(ponderation))):
        ponderation1.append(str(ponderation[i])[1:-2])
    print(ponderation1)
    for i in range((len(ponderation))):
        nbr_exam.append("NOTE" + str(i + 1))

    bar_labels = labels
    bar_values = values
    return render_template('prevision.html', max=100, labels=nbr_exam, values=note1,title=info1)

@app.route("//Prevision/Calcul5")
def Calcul5():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" + info5 + "'" + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    totaux = []
    nbr_exam = []
    for i in range((len(note))):
        totaux.append(str(100))
        note1.append(str(note[i])[1:-2])
    print(note)
    cmd = 'SELECT n.ponderation FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    ponderation = cur.fetchall()
    ponderation1 = []
    nbr_exam = []
    for i in range((len(ponderation))):
        ponderation1.append(str(ponderation[i])[1:-2])
    print(ponderation1)
    for i in range((len(ponderation))):
        nbr_exam.append("NOTE" + str(i + 1))

    bar_labels = labels
    bar_values = values
    return render_template('prevision.html', max=100, labels=nbr_exam, values=note1,title=info1)
@app.route("//Prevision/Calcul6")
def Calcul6():
    cmd = 'SELECT c.sigleCours FROM Cours c WHERE c.nom=' + "'" + info6 + "'" + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    sigleCours = str(cur.fetchone())[2:-3]

    cmd = 'SELECT n.note FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    note = cur.fetchall()
    note1 = []
    totaux = []
    nbr_exam = []
    for i in range((len(note))):
        totaux.append(str(100))
        note1.append(str(note[i])[1:-2])
    print(note)
    cmd = 'SELECT n.ponderation FROM Note n  WHERE n.sigleCours =' + "'" + sigleCours + "'" + 'and n.idul = ' + idul + ';'
    print(cmd)
    cur = conn.cursor()
    cur.execute(cmd)
    ponderation = cur.fetchall()
    ponderation1 = []
    nbr_exam = []
    for i in range((len(ponderation))):
        ponderation1.append(str(ponderation[i])[1:-2])
    print(ponderation1)
    for i in range((len(ponderation))):
        nbr_exam.append("NOTE" + str(i + 1))

    bar_labels = labels
    bar_values = values
    return render_template('prevision.html', max=100, labels=nbr_exam, values=note1,title=info1)
if __name__ == "__main__":
    app.run()