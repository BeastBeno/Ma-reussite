

a = [50, 80]
b = [0.25, 0.25]
c = [100, 100]

moyenneaatteindre = 99
coeffdufinal = 0.5
totaldufinal = 100

def atteindre(notes, coefficients, totaux, moyenneaatteindre, coeffdufinal, totaldufinal):
    x = 0.

    notes.append(x)
    coefficients.append(coeffdufinal)
    totaux.append(totaldufinal)
    moyenne = 0
    a = len(notes)

    while moyenne != moyenneaatteindre:
        x += 1
        notes[a-1] = x

        somme = 0
        maximum = 0
        print(notes)
        for i in range (len(notes)):


            somme+=float(notes[i])*float(coefficients[i])
            maximum+=float(totaux[i])*float(coefficients[i])
            moyenne=somme*100/maximum
        print(moyenne)

    return x

def moyenne_ponderee(notes,coefficients,totaux):
    """ Cacul d'une moyenne pondérée à partir d'une liste de notes et d'une liste de coefficients"""
    somme=0
    maximum=0
    moyenne = 0
    for i in range (len(notes)):
        somme+=float(notes[i])*float(coefficients[i])
        maximum+=float(totaux[i])*float(coefficients[i])
        moyenne=somme*100/maximum
    return moyenne

print(moyenne_ponderee(a, b, c))

print(atteindre(a,b,c,moyenneaatteindre,coeffdufinal,totaldufinal))