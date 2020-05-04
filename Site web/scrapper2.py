import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver






                #('MAT-1910',  'Math de ingenieur I', 3, 4, 'MAT-0260', 'GLO,GIF,GEL,GPH,GEX,GCI,GMC,GMN,GIN', 'o,o,o,o,o,o,o,o,o')

lienprog = ['https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-chimique-b-ing.html?tx_oful_pi1%5Bprint%5D=1'#,
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-civil/',
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-des-eaux/',
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-cooperatif-en-genie-des-mines-et-de-la-mineralurgie/',
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-geologique/'
                #,'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-logiciel/',
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-cooperatif-en-genie-des-materiaux-et-de-la-metallurgie/'
                ]
for un in lienprog:
    obligatoire, option, concentration = [], [], []
    newurl = un
    newresponse = requests.get(newurl)
    soups = BeautifulSoup(newresponse.text, 'html5lib')

    a = soups.find('div', {'id' : 'structure-programme_content'}).find('div', {'class' : 'contenu'})
    nomprogramme = a.find('table', {'class' : 'titrebloc'}).find('td', {'class' : 'col1'}).find('span').text


    b = a.findAll('div', {'class': 'section'})
    print("Le programme choisi est " + nomprogramme)
    for variante in b:
        if variante.find('div', {'class' : 'titresection'}).text == 'Activités de formation communes':
            c = variante.parent.find(lambda tag: tag.name == 'table' and
                                   tag.get('class') == ['cours']).findAll('a')
            for var in c:
                db = var['href']
                if not 'https://www.ulaval.ca' + db in obligatoire:
                    obligatoire.append('https://www.ulaval.ca' + db)
            print(obligatoire)

        if variante.find('div', {'class': 'titresection'}).text == 'Autres activités':
            c = variante.findAll('div', {'class' : 'regle'})
            for var in c:
                liste = []
                nomregle = var.find('div', {'class' : 'titreregle'}).text
                if nomregle == 'Règle 1 - 3 crédits' or nomregle == 'Règle 2 - 3 crédits' or nomregle == 'Règle 3 - 3 crédits' \
                    or nomregle == 'Règle 4 - 3 crédits'or nomregle == 'Règle 5 - 3 crédits'or nomregle == 'Règle 6 - 3 crédits'or \
                    nomregle == 'Règle 7 - 3 crédits' or nomregle == 'Règle 3 - Un cours parmi:':
                    dbnew = 3

                else:
                    dbnew = int(nomregle[nomregle.find(' - ')+2:nomregle.find(' à')])
                    if dbnew == 0:
                        dbnew = int(nomregle[nomregle.find('à ')+2:nomregle.find(' crédits')])



                o = var.findAll('a')


                for unique in o:

                    db = unique['href']
                    if not 'https://www.ulaval.ca' + db in liste:
                        liste.append('https://www.ulaval.ca' + db)
                option.append({nomregle[0:7]: {str(dbnew) + ' crédits': liste}})



            print(option)

        if variante.find('div', {'class': 'titresection'}).text == 'Concentrations':
            c = variante.findAll(lambda tag: tag.name == 'div' and
                                                 tag.get('class') == ['bloc'])
            for vari in c:
                listeregle = []
                nomconcentration = vari.find('td', {'class' : 'col1'}).text
                creditconcentration = vari.find('td', {'class' : 'col3'}).text
                regle = vari.findAll('div', {'class' : 'regle'})
                for z in regle:

                    liste = []

                    nomregle = z.find('div', {'class': 'titreregle'}).text

                    if nomregle == 'Règle 1 - 3 crédits' or nomregle == 'Règle 2 - 3 crédits' or nomregle == 'Règle 3 - 3 crédits' \
                            or nomregle == 'Règle 4 - 3 crédits' or nomregle == 'Règle 5 - 3 crédits' or nomregle == 'Règle 6 - 3 crédits' or \
                            nomregle == 'Règle 7 - 3 crédits' or nomregle == 'Règle 3 - Un cours parmi:':
                        dbnew = 3

                    else:
                        dbnew = int(nomregle[nomregle.find(' - ') + 2:nomregle.find(' à')])
                        if dbnew == 0:
                            dbnew = int(nomregle[nomregle.find('à ') + 2:nomregle.find(' crédits')])

                    o = z.findAll('a')


                    for unique in o:

                        db = unique['href']

                        if not 'https://www.ulaval.ca' + db in liste:
                            liste.append('https://www.ulaval.ca' + db)
                    listeregle.append({nomregle[0:7]: {str(dbnew) + ' crédits': liste}})
                concentration.append({nomconcentration: {creditconcentration: listeregle}})
            print(concentration)


    
















