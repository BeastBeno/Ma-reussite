import requests
from bs4 import BeautifulSoup
import random

# ('MAT-1910',  'Math de ingenieur I', 3, 4, 'MAT-0260', 'GLO,GIF,GEL,GPH,GEX,GCI,GMC,GMN,GIN', 'o,o,o,o,o,o,o,o,o')

lienprog = [
    'https://www.ulaval.ca/les-etudes/cours/repertoire/detailsCours/gel-3003-signaux-et-systemes-discrets.html#renseignements'#,
    #'https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-logiciel-b-ing.html#description-officielle&structure-programme',
    # 'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-des-eaux/',
    # 'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-cooperatif-en-genie-des-mines-et-de-la-mineralurgie/',
    # 'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-geologique/'
    # ,'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-logiciel/',
    # 'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-cooperatif-en-genie-des-materiaux-et-de-la-metallurgie/'
]
def tablecours(variable):

    newurl = variable
    newresponse = requests.get(newurl)
    soups = BeautifulSoup(newresponse.text, 'html5lib')
    a = soups.find('div', {'id': 'contenuFiche'})
    code = a.find('h1', {'class': 'fiche'}).contents
    sigle = code[0][0:8]
    nomcours = a.find('h1', {'class': 'fiche'}).find('span').text

    credit = a.find('div', {'class': 'bloc renseignements'}).find('div', {'class' : 'droite'}).contents
    vraicredit = credit[0]

    return sigle, nomcours, int(vraicredit), 8

