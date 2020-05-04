
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)

<<<<<<< HEAD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pr@j?vision100%@$!'
app.config['MYSQL_DB'] = 'bd_universitaire'

mysql = MySQL(app)
@app.route('/bd_universitaire/', methods=['GET', 'POST'])
def login():
    return render_template('../mon site web/Sanstitre-2.html', msg='')
=======
@app.route("/")
def chart():
    return render_template('../Site web/Connexion - Université Laval.html')

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=5001)


>>>>>>> 3f00456aa2c21a72fba8fec3c843aaf68e607949

if __name__ == "__main__":
    app.run()
