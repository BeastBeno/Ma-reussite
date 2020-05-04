import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




url = 'https://www.fsg.ulaval.ca/etudes/genie/'

response = requests.get(url)
if response.ok:
    ref, lienprogramme = [], []
    soup = BeautifulSoup(response.text, 'lxml')
    b = soup.findAll('a', {'class': 'btn-pour-en-savoir-plus'})
    for a in b:
        lien = a['href']
        ref.append('https://www.fsg.ulaval.ca' + lien)
    for a in ref:
        newurl = a
        newresponse = requests.get(newurl)
        soups = BeautifulSoup(newresponse.text, 'lxml')
        c = soups.findAll('a', {'class': 'bouton bouton-deuxtierstiers fond-rouge'})
        for d in c:
            liens = d['href']
            if liens.find('baccalaureat') != -1 and not 'https://www.fsg.ulaval.ca' + liens in lienprogramme:
                lienprogramme.append('https://www.fsg.ulaval.ca' +liens)
                #('MAT-1910',  'Math de ingenieur I', 3, 4, 'MAT-0260', 'GLO,GIF,GEL,GPH,GEX,GCI,GMC,GMN,GIN', 'o,o,o,o,o,o,o,o,o')

    lienprog = ['https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-chimique/'#,
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-civil/',
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-des-eaux/',
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-cooperatif-en-genie-des-mines-et-de-la-mineralurgie/',
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-geologique/'
                #,'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-en-genie-logiciel/',
                #'https://www.fsg.ulaval.ca/etudes/programmes-detudes/baccalaureat-cooperatif-en-genie-des-materiaux-et-de-la-metallurgie/'
                ]
    for un in lienprog:
        obligatoire, option, = [], []
        newurl = un
        newresponse = requests.get(newurl)
        soups = BeautifulSoup(newresponse.text, 'lxml')
        c0 = soups.findAll('section', {'class': 'strate fond-gris-bleu-pale'})
        for i in c0:
            war = i.find('header').find('h1').text
            print(war)
            break
        for i in c0:

            var = i.findAll('section', {'class': 'strate-contenu'} )
            for z in var:
                var1 = z.findAll('article', {'class': 'accordeon fond-gris-bleu-pale'})
                for w in var1:
                    var2 = w.find('button', {'type': 'button'}, )
                    if var2.text == 'Structure du programme':

                        var3 = w.findAll('header')
                        for r in var3:

                            if r.find('h4').text == 'Activités de formation communes':

                                var4 = r.parent.find('table', {'class': 'property'}).findAll('a')
                                for lien in var4:
                                    liens = lien['href']
                                    if not liens in obligatoire:
                                        obligatoire.append(liens)
                                print(obligatoire)
                            if r.find('h4').text == 'Autres activités':
                                var4 = r.parent.find('table', {'class': 'block'}).findAll('h6', {'class': 'regle'})
                                a = []
                                for lien in var4:

                                    bc = []

                                    if not (lien.text == 'Règle 3 - 3 crédits' or lien.text == 'Règle 2 - 3 crédits' or lien.text == 'Règle 1 - 3 crédits'
                                    or lien.text == 'Règle 4 - 3 crédits' or lien.text == 'Règle 5 - 3 crédits' or lien.text == 'Règle 6 - 3 crédits' ) or not lien.parent.find('span', {
                                        'class': 'ulavalExigenceCoursCode'}):


                                        var5 = lien.parent.find('table', {'class': 'property'}).findAll('a')

                                        for otherlien in var5:
                                            liens = otherlien['href']
                                            if not liens in bc:
                                                bc.append(liens)

                                        if lien.text[10] != '0' and not lien.text[11].isdigit:


                                            newvar = lien.text[10]

                                            a.append({lien.text[0:7]: {newvar + ' crédits': bc}})
                                        if lien.text[10] == '0':
                                            newvar = lien.text[14]
                                            a.append({lien.text[0:7]: {newvar + ' crédits': bc}})
                                        elif lien.text[10] != '0' and lien.text[11].isdigit:
                                            newvar = lien.text[10] + lien.text[11]
                                            a.append({lien.text[0:7]: {newvar + ' crédits': bc}})

                                print(a)

                            if r.find('h4').text == 'Concentrations':

                                concentrations = {}
                                listeconcentration = []
                                var4 = r.parent.findAll('table', {'class': 'block'})
                                for zb in var4:
                                    az = zb.find('h5') #concentration

                                    aa = az.parent.parent.parent.parent.findAll('h6', {'class': 'regle'}) #listerègle
                                    concentration = {}
                                    for lien in aa:


                                        bcd = []
                                        if lien.text == 'Règle 1 - 3 crédits'and lien.parent.find('div', {'class': 'en-evidence regroupement'}): # sans concentration

                                            var5 = lien.parent.parent.find('table', {'class': 'property'}).findAll('a')
                                            for otherlien in var5:
                                                liens = otherlien['href']

                                                if not liens in bcd:
                                                    bcd.append(liens)
                                            newvar = lien.parent.parent.parent.parent.parent.find('span', {'class': 'h5'}).text

                                            concentration['None'] = {newvar + ' crédits': bcd}
                                            concentrations[az.text] = concentration

                                        if not lien.parent.find('div', {'class': 'en-evidence regroupement'}):


                                            var5 = lien.parent.find('table', {'class': 'property'}).findAll('a')

                                            for otherlien in var5:
                                                liens = otherlien['href']
                                                if not liens in bcd:
                                                     bcd.append(liens)

                                            if lien.text[10] == '0':

                                                newvar = lien.text[14]
                                                concentration[lien.text[0:7]] = {newvar + ' crédits': bcd}
                                                concentrations[az.text] = concentration

                                            elif lien.text[10] != '0' and not lien.text[11].isdigit:

                                                newvar = lien.text[10]

                                                concentration[lien.text[0:7]] = {newvar + ' crédits': bcd}
                                                concentrations[az.text] = concentration
                                            elif lien.text[10] != '0' and lien.text[11].isdigit:
                                                newvar = lien.text[10] + lien.text[11]
                                                concentration[lien.text[0:7]] = {newvar + ' crédits': bcd}
                                                concentrations[az.text] = concentration






                                print(concentrations)

















