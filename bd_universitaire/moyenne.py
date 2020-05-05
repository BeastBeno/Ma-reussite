

a = [65, 81.25]
b = [0.3, 0.35]
c = [100, 100]

moyenneaatteindre = 81.19
coeffdufinal = 0.35
totaldufinal = 100

def atteindre(notes, coefficients, totaux, moyenneaatteindre, coeffdufinal, totaldufinal):
    x = 0.

    notes.append(x)
    coefficients.append(coeffdufinal)
    totaux.append(totaldufinal)
    moyenne = 0
    a = len(notes)

    while moyenne != moyenneaatteindre:
        x += 0.01
        notes[a-1] = x

        somme = 0
        maximum = 0

        for i in range (len(notes)):


            somme+=float(notes[i])*float(coefficients[i])
            maximum+=float(totaux[i])*float(coefficients[i])
            moyenne=round(somme*100/maximum,2)


    return round(x, 2)

def moyenne_ponderee(notes,coefficients,totaux):
    """ Cacul d'une moyenne pondérée à partir d'une liste de notes et d'une liste de coefficients"""
    somme=0
    maximum=0
    moyenne = 0
    for i in range (len(notes)):
        somme+=float(notes[i])*float(coefficients[i])
        maximum+=float(totaux[i])*float(coefficients[i])
        moyenne= round(somme*100/maximum,2)
    return moyenne

print(moyenne_ponderee(a, b, c))

print(atteindre(a,b,c,moyenneaatteindre,coeffdufinal,totaldufinal))