import pymysql
from flask import Flask , render_template , request, Markup
import pymysql.cursors
conn = pymysql.connect(host='localhost',
                           user='root',
                           password='Reussite2019',
                           db='bd_universitaire')

info1 = 'Analyse économique en ingénierie'
note = ((80.0,),)
note1 = []

for i in range((len(note))):
    note1.append(str(note[i])[1:-2])
for i in note1:
    print(i)