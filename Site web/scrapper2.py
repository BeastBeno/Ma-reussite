import requests
from bs4 import BeautifulSoup
from scrapper import tablecours
import ast






                #('MAT-1910',  'Math de ingenieur I', 3, 4, 'MAT-0260', 'GLO,GIF,GEL,GPH,GEX,GCI,GMC,GMN,GIN', 'o,o,o,o,o,o,o,o,o')

lienprog = ['https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-chimique-b-ing.html?tx_oful_pi1%5Bprint%5D=1',
                'https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-logiciel-b-ing.html#description-officielle&structure-programme',
                'https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-industriel-b-ing.html#description-officielle&structure-programme',
                'https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-civil-b-ing.html#description-officielle&structure-programme',
                'https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-des-eaux-b-ing.html#description-officielle&structure-programme'
                ,'https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-electrique-b-ing.html#description-officielle&structure-programme',
                'https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-geologique-b-ing.html#description-officielle&structure-programme',
                'https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-informatique-b-ing.html#description-officielle&structure-programme',
                'https://www.ulaval.ca/les-etudes/programmes/repertoire/details/baccalaureat-en-genie-physique-b-ing.html#description-officielle&structure-programme'
                ]
gang = []
gang1 = []
incre = 0
incre1 = 0
nombre = []
for un in lienprog:
    listeprog = [{'Génie civil' :'GCI'},{'Génie des eaux':'GEX'},{'Génie chimique'  :'GCH'},{'Génie industriel' :'GIN'},
                 {'Génie électrique' :'GEL'},{'Génie logiciel' :'GLO'},{'Génie géologique' :'GGL'},{'Génie informatique' :'GIF'},
                 {'Génie physique' :'GPH'}]
    for i in range(100):
        nombre.append(str(i))




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
            c = variante.findAll('a')
            for var in c:
                db = var['href']
                if not 'https://www.ulaval.ca' + db in obligatoire:
                    obligatoire.append('https://www.ulaval.ca' + db)
            print(obligatoire)

        if variante.find('div', {'class': 'titresection'}).text == 'Autres activités':
            c = variante.findAll('div', {'class' : 'regle'})
            for var in c:
                dbnew = 0
                liste = []
                numeroregle = []
                nombrecredit = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
                for op in range(11):
                    numeroregle.append(op)

                nomregle = var.find('div', {'class': 'titreregle'}).text

                for abc in numeroregle:
                    for aze in nombrecredit:
                        for azb in nombrecredit:

                            if nomregle == 'Règle ' + str(abc) + ' - ' + str(aze) + ' crédits':
                                dbnew = aze
                            if nomregle == 'Règle ' + str(abc) + ' - ' + str(aze) + ' crédits parmi:':
                                dbnew = aze
                            if nomregle == 'Règle 3 - Un cours parmi:':
                                dbnew = 3
                            if nomregle == 'Règle ' + str(abc) + ' - ' + str(aze) + ' à ' + str(
                                    azb) + ' crédits parmi:':

                                if aze == 0:
                                    dbnew = azb
                                else:
                                    dbnew = aze



                o = var.findAll('a')


                for unique in o:

                    db = unique['href']
                    if not 'https://www.ulaval.ca' + db in liste:
                        liste.append('https://www.ulaval.ca' + db)
                option.append({nomregle[6]: {str(dbnew) : liste}})



            print(option)

        if variante.find('div', {'class': 'titresection'}).text == 'Concentrations':
            c = variante.findAll(lambda tag: tag.name == 'div' and
                                                 tag.get('class') == ['bloc'])
            for vari in c:
                compteur = 0
                comparaison = []

                listeregle = []
                nomconcentration = vari.find('td', {'class' : 'col1'}).text
                creditconcentration = vari.find('td', {'class' : 'col3'}).text
                oblig = vari.find('table', {'class': 'cours'}).findAll('a')
                for uni in oblig:
                    db = uni['href']

                    if not 'https://www.ulaval.ca' + db in comparaison:
                        comparaison.append('https://www.ulaval.ca' + db)
                for untruc in listeprog:
                    for azer in untruc.keys():
                        if azer == nomprogramme:
                            incre += 1
                            gang.append((incre, nomconcentration, untruc.get(azer)))





                regle = vari.findAll('div', {'class' : 'regle'})


                for z in regle:
                    compteur += 1
                    dbnew = 0
                    liste = []
                    numeroregle = []
                    nombrecredit = [0, 3, 6, 7, 9, 12, 15, 18, 21, 24, 27, 30]
                    for op in range(11):
                        numeroregle.append(op)

                    nomregle = z.find('div', {'class': 'titreregle'}).text


                    for abc in numeroregle:
                        for aze in nombrecredit:
                            for azb in nombrecredit:

                                if nomregle == 'Règle ' + str(abc) + ' - ' + str(aze) + ' crédits':

                                    dbnew = aze
                                if nomregle == 'Règle ' + str(abc) + ' - ' + str(aze) + ' crédits parmi:':
                                    dbnew = aze
                                if nomregle == 'Règle 3 - Un cours parmi:':
                                    dbnew = 3
                                if nomregle == 'Règle ' + str(abc) + ' - ' + str(aze) + ' à ' + str(azb) + ' crédits parmi:':

                                    if aze == 0:
                                        dbnew = azb
                                    else:
                                        dbnew = aze


                    o = z.findAll('a')


                    for unique in o:

                        db = unique['href']

                        if not 'https://www.ulaval.ca' + db in liste:
                            liste.append('https://www.ulaval.ca' + db)
                    if comparaison != liste and compteur == 1:
                        creditobli = 0
                        for i in comparaison:
                            creditobli += 3
                        if not {'obligatoire': {str(creditobli) + ' crédits': comparaison}} in listeregle:
                            listeregle.append({'obligatoire': {str(creditobli) + ' crédits': comparaison}})
                    listeregle.append({nomregle[6]: {str(dbnew): liste}})
                concentration.append({nomconcentration: {creditconcentration + ' crédits': listeregle}})
            print(concentration)

    # ('GEL-3003', 'A')
    # (123, 'GLO', 'MAT-1910', 'o', 'H', '3', '9', 'Études-travail')
    # (id, sigleProgramme, sigleCours,typeCours,disponibilite, regle, creditRegle, nomConcentration)

    for i in obligatoire:
        print(i)

        for untruc in listeprog:
            for azer in untruc.keys():
                if azer == nomprogramme:
                    incre1 += 1

                    variable = tablecours(i)
                    gang1.append(str((incre1, untruc.get(azer), variable[0], 'o', variable[1], 'null', 'null', 'null')) + ',')

    for i in option:
        for untruc in listeprog:
            for azer in untruc.keys():
                if azer == nomprogramme:

                    for regle in i.items():


                        for credit in regle[1].items():
                            for cours in credit[1]:
                                incre1 += 1

                                variable = tablecours(cours)
                                gang1.append(str((incre1, untruc.get(azer), variable[0], 'p', variable[1], regle[0],
                                                  credit[0], 'null')) + ',')
                        # ('GEL-3003', 'A')
                        # (123, 'GLO', 'MAT-1910', 'o', 'H', '3', '9', 'Études-travail')
                        # (id, sigleProgramme, sigleCours,typeCours,disponibilite, regle, creditRegle, nomConcentration)


        

    for i in concentration:
        for untruc in listeprog:
            for azer in untruc.keys():
                if azer == nomprogramme:

                    for concentr in i.items():

                        for credit in concentr[1].items():


                            for listregl in credit[1]:
                                for u in listregl.items():
                                    for l in u[1].items():
                                        for newcours in l[1]:

                                            incre1 += 1
                                            varq = ''
                                            for num in nombre:
                                                if u[0] == num:
                                                    varq = 'p'
                                                if u[0] == 'obligatoire':
                                                    varq = 'o'

                                            variable = tablecours(newcours)
                                            gang1.append(
                                                str((incre1, untruc.get(azer), variable[0], varq, variable[1], u[0],
                                                     l[0], concentr[0])) + ',')

fichier = open("listeAppartient.txt", "w")
for i in gang1:
    fichier.write(i + "\n")
fichier.close()














'''
    fichier = open("listeCours.txt", "r+")

    for i in obligatoire:
        listefich = []
        variable = tablecours(i)
        for az in fichier:
            listefich.append(az)


        if not variable in listefich:



            fichier.write(str(variable) + "\n")

    for i in option:
        for a in i.values():
            for z in a.values():
                for e in z:
                    variable = tablecours(e)
                    listefich = []
                    for az in fichier:
                        listefich.append(az)
                    if not variable in listefich:
                        fichier.write(str(variable) + "\n")
    fichier.close()

'''
'''

    (122, 'Traitement de donnees massive', 'GLO');
'''

'''
fichier = open("listeConcentration.txt", "w")
for yes in gang:
    fichier.write(str(yes)+ "," + "\n")
fichier.close()

'''














