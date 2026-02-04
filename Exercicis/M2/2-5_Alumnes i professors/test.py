from estudiant import Estudiant
from professor import Professor
from persona import Persona
from assignatura import Assignatura

grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")

print("Comment :=>> ")
print("Comment :=>> Test de la classe Persona")
print("Comment :=>> =========================")
reduccio = 0.0
dadesPersona = ("niu_1", "nom_1")
assignatures = [[], [("assig_1", 6, 12)], [("assig_1", 6, 6),
                                           ("assig_2", 3, 6), ("assig_3", 6, 4), ("assig_4", 9, 10)]]
nomsCerca = [["assig_1"], ["assig_1", "assig_2"],
             ["assig_1", "assig_2", "assig_4", "assig_5"]]
resultatEsperat = [[False], [True, False], [True, True, True, False]]
i = 1
for assig, noms, resultats in zip(assignatures, nomsCerca, resultatEsperat):
    print("TEST: ", i)
    i += 1
    p = Persona(dadesPersona[0], dadesPersona[1])
    print("Comment :=>> Inicialitzant objecte de la classe Persona amb valors:")
    print("Comment :=>> Niu: ", dadesPersona[0])
    print("Comment :=>> Nom: ", dadesPersona[1])
    print("Comment :=>> ----------")
    print("Comment :=>> Afegint assignatures ...")
    for a in assig:
        print("Comment :=>> Dades de l'assignatura: ", a[0], a[1], a[2])
        p.afegeixAssignatura(Assignatura(a[0], a[1], a[2]))
    for n, re in zip(noms, resultats):
        print("Comment :=>> --------------------------------")
        print("Comment :=>> Buscant si existeix assignatura: ", n)
        print("Comment :=>> ----------")
        print("Comment :=>> Resultat esperat", re)
        ro = p.cercaAssignatura(n)
        print("Comment :=>> ----------")
        print("Comment :=>> Resultat obtingut", ro)
        if (ro == re):
            print("Comment :=>> CORRECTE")
        else:
            print("Comment :=>> ERROR")
            reduccio = reduccio + 1.0
    print("Comment :=>> -------------------------------------------------------")

if (reduccio > 6):
    reduccio = 6
grade = grade + (4 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ")
print("Comment :=>> Test de la classe Estudiant")
print("Comment :=>> ===========================")
reduccio = 0.0
dadesEstudiant = ("niu_1", "nom_1", "titulacio_1")
assignatures = [[], [("assig_1", 6, 12)], [("assig_1", 6, 6),
                                           ("assig_2", 3, 6), ("assig_3", 6, 4), ("assig_4", 9, 10)]]
nomsCerca = [["assig_1"], ["assig_1", "assig_2"],
             ["assig_1", "assig_2", "assig_4", "assig_5"]]
resultatEsperat = [[False], [True, False], [True, True, True, False]]
nCreditsEsperat = [0, 6, 24]
i = 1
e = Estudiant(dadesEstudiant[0], dadesEstudiant[1], dadesEstudiant[2])
print("Comment :=>> Inicialitzant objecte de la classe Estudiant amb valors:")
print("Comment :=>> Niu: ", dadesEstudiant[0])
print("Comment :=>> Nom: ", dadesEstudiant[1])
print("Comment :=>> Titulacio: ", dadesEstudiant[2])
print("Comment :=>> ----------")
print("Comment :=>> Comprovant valors de l'objecte Estudiant despres de la inicialitacio:")
print("Comment :=>> Niu: ", e.get_niu())
print("Comment :=>> Nom: ", e.get_nom())
print("Comment :=>> Titulacio: ", e.get_titulacio())
print("Comment :=>> -------------------------------------------------------")
if e.get_niu() != dadesEstudiant[0] or e.get_nom() != dadesEstudiant[1] or e.get_titulacio() != dadesEstudiant[2]:
    print("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
else:
    print("Comment :=>> CORRECTE")
for assig, noms, resultats, nCredits in zip(assignatures, nomsCerca, resultatEsperat, nCreditsEsperat):
    print("TEST: ", i)
    i += 1
    print("Comment :=>> --------------------------------")
    print("Comment :=>> Afegint assignatures ...")
    for a in assig:
        print("Comment :=>> Dades de l'assignatura: ", a[0], a[1], a[2])
        e.afegeixAssignatura(Assignatura(a[0], a[1], a[2]))
    print("Comment :=>> --------------------------------")
    print("Comment :=>> Comprovant numero de credits matriculats...")
    print("Comment :=>> ----------")
    print("Comment :=>> Resultat esperat", nCredits)
    nc = e.creditsMatriculats()
    print("Comment :=>> ----------")
    print("Comment :=>> Resultat obtingut", nc)
    if (nc == nCredits):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    for n, re in zip(noms, resultats):
        print("Comment :=>> --------------------------------")
        print("Comment :=>> Buscant si existeix assignatura: ", n)
        print("Comment :=>> ----------")
        print("Comment :=>> Resultat esperat", re)
        ro = e.cercaAssignatura(n)
        print("Comment :=>> ----------")
        print("Comment :=>> Resultat obtingut", ro)
        if (ro == re):
            print("Comment :=>> CORRECTE")
        else:
            print("Comment :=>> ERROR")
            reduccio = reduccio + 1.0
    print("Comment :=>> -------------------------------------------------------")

if (reduccio > 6):
    reduccio = 6
grade = grade + (3 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ")
print("Comment :=>> Test de la classe Professor")
print("Comment :=>> ===========================")
reduccio = 0.0
dadesProfessor = ("niu_1", "nom_1", "departament_1", 24)
assignatures = [[], [("assig_1", 6, 12)], [("assig_1", 6, 6),
                                           ("assig_2", 3, 6), ("assig_3", 6, 4), ("assig_4", 9, 10)]]
nomsCerca = [["assig_1"], ["assig_1", "assig_2"],
             ["assig_1", "assig_2", "assig_4", "assig_5"]]
resultatEsperat = [[False], [True, False], [True, True, True, False]]
nCreditsEsperat = [0, 12, 26]
i = 1
p = Professor(dadesProfessor[0], dadesProfessor[1],
              dadesProfessor[2], dadesProfessor[3])
print("Comment :=>> Inicialitzant objecte de la classe Professor amb valors:")
print("Comment :=>> Niu: ", dadesProfessor[0])
print("Comment :=>> Nom: ", dadesProfessor[1])
print("Comment :=>> Departament: ", dadesProfessor[2])
print("Comment :=>> Maxim Credits: ", dadesProfessor[3])
print("Comment :=>> ----------")
print("Comment :=>> Comprovant valors de l'objecte Estudiant despres de la inicialitacio:")
print("Comment :=>> Niu: ", p.get_niu())
print("Comment :=>> Nom: ", p.get_nom())
print("Comment :=>> Departament: ", p.get_departament())
print("Comment :=>> Maxim Credits: ", p.get_maximCredits())
print("Comment :=>> -------------------------------------------------------")
if p.get_niu() != dadesProfessor[0] or p.get_nom() != dadesProfessor[1] or p.get_departament() != dadesProfessor[2]:
    print("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
else:
    print("Comment :=>> CORRECTE")
for assig, noms, resultats, nCredits in zip(assignatures, nomsCerca, resultatEsperat, nCreditsEsperat):
    p = Professor(dadesProfessor[0], dadesProfessor[1],
                  dadesProfessor[2], dadesProfessor[3])
    print("TEST: ", i)
    print("Comment :=>> Inicialitzant objecte de la classe Professor amb valors:")
    print("Comment :=>> Niu: ", dadesProfessor[0])
    print("Comment :=>> Nom: ", dadesProfessor[1])
    print("Comment :=>> Departament: ", dadesProfessor[2])
    print("Comment :=>> Maxim Credits: ", dadesProfessor[3])
    i += 1
    print("Comment :=>> --------------------------------")
    print("Comment :=>> Afegint assignatures ...")
    for a in assig:
        print("Comment :=>> Dades de l'assignatura: ", a[0], a[1], a[2])
        p.afegeixAssignatura(Assignatura(a[0], a[1], a[2]))
    print("Comment :=>> --------------------------------")
    print("Comment :=>> Comprovant numero de credits impartits...")
    print("Comment :=>> ----------")
    print("Comment :=>> Resultat esperat", nCredits)
    nc = p.creditsImpartits()
    print("Comment :=>> ----------")
    print("Comment :=>> Resultat obtingut", nc)
    if (nc == nCredits):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    for n, re in zip(noms, resultats):
        print("Comment :=>> --------------------------------")
        print("Comment :=>> Buscant si existeix assignatura: ", n)
        print("Comment :=>> ----------")
        print("Comment :=>> Resultat esperat", re)
        ro = p.cercaAssignatura(n)
        print("Comment :=>> ----------")
        print("Comment :=>> Resultat obtingut", ro)
        if (ro == re):
            print("Comment :=>> CORRECTE")
        else:
            print("Comment :=>> ERROR")
            reduccio = reduccio + 1.0
    print("Comment :=>> -------------------------------------------------------")

if (reduccio > 6):
    reduccio = 6
grade = grade + (3 - reduccio)


if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
