from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Reussite2019'
app.config['MYSQL_DB'] = 'bd_universitaire'

mysql = MySQL(app)
@app.route('/bd_universitaire/', methods=['GET', 'POST'])
def login():
    return render_template('index.html', msg='')



