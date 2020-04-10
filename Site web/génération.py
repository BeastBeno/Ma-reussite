import random
import string

lis, newsigle, sigle, siglefinal = [], [], [], []
sigleprogramme = ["GMC,	Génie mécanique", "GCI,	Génie civil", "GEX,	Génie des eaux", "ENV, Environnement", "GCH, Génie chimique", "GIN,	Génie industriel", "GEL, Génie électrique", "GLO, Génie logiciel", "GGL, Génie géologique", "GMN, Génie des mines et de la minéralurgie", "GIF,	Génie informatique", "GPH, Génie physique"]

for i in sigleprogramme:
    a = i.split(",")
    newsigle.append(a)

for i in newsigle:
    sigle.append(i[0])
    siglefinal.append("('" + i[0] + "', '" + i[1] + "' , 120)")
fichier = open("listeSigle.txt", "w")
for char in siglefinal:
    fichier.write("\n" + char)
fichier.close()





def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
#('DIBAX', 'Baxter Dieter', 'jsbvssdsd', 1, 0, 'GLO')
#('GLO', 'Genie Logiciel', 120)
with open('nom prenom.txt', 'r') as fich:
    fichier = open("listeEtudiant.txt", "w")
    for ligne in fich.readlines():

        li = ligne.split(",")

        a = li[0]
        liste = []
        liste.append(a)

        liste.append(li[1][:-2])
        print(liste)
        idul = liste[1][:2] + liste[0][:3]
        idul = idul.upper()
        print(idul)
        lis.append(idul)

        b = "('" + idul + "', " + "'" + liste[1] + " " + liste[0] + "'" + ", " + "'" + randomStringDigits(8) +", " + str(random.randrange(0, 10)) + ", " + str(random.randrange(0, 120)) + ", '" + random.choice(sigle) + "')"
        fichier.write("\n" + b)
    fichier.close()
for x in range(len(lis)):
    for y in range(x+1, len(lis)):
        if lis[x] == lis[y]:
            print(1)