import activitat as a
import usuari as u

grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")

print("Comment :=>> ")
print("Comment :=>> Test de la classe Usuari")
print("Comment :=>> ========================")
reduccio = 0.0
usuaris = [("codi_1", "usuari_1", 20), ("codi_2", "usuari_2", 17),
           ("codi_1", "usuari_1", 20), ("codi_2", "usuari_2", 17), ]
resultatEsperat = [True, False, True, False]
tipusInit = [0, 0, 1, 1]
for us, re, ti in zip(usuaris, resultatEsperat, tipusInit):
    print("Comment :=>> -------------------------------------------------------")
    if (ti == 0):
        print("Comment :=>> Inicialitzant usuari amb el constructor de la classe amb els valors:")
    else:
        print("Comment :=>> Inicialitzant usuari amb els setters amb els valors:")
    print("Comment :=>> Codi: ", us[0])
    print("Comment :=>> Nom: ", us[1])
    print("Comment :=>> Edat: ", us[2])
    print("Comment :=>> ---")
    if (not re):
        print("Comment :=>> Resultat esperat: EXCEPCIO")
        print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut despres inicialitzacio:")
    try:
        if (ti == 0):
            usr = u.Usuari(us[0], us[1], us[2])
        else:
            usr = u.Usuari()
            usr.codi = us[0]
            usr.nom = us[1]
            usr.edat = us[2]
        resultat = True
        print("Comment :=>> Codi: ", usr.codi)
        print("Comment :=>> Nom: ", usr.nom)
        print("Comment :=>> Edat: ", usr.edat)
    except AssertionError:
        print("Comment :=>> EXCEPCIO")
        resultat = False
    if (resultat == re):
        if (resultat):
            if (usr.codi == us[0]) and (usr.nom == us[1]) and (usr.edat == us[2]):
                print("Comment :=>> CORRECTE")
            else:
                print("Comment :=>> ERROR")
                reduccio = reduccio + 1.0
        else:
            print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ")
print("Comment :=>> Test d'inicialitzacio de la classe Activitat")
print("Comment :=>> ============================================")
reduccio = 0.0
activitats = [("activitat_1", 20, 18, 80, "dilluns", "10:00"), ("activitat_1", 50,
                                                                18, 80, "dilluns", "10:00"), ("activitat_1", 20, 10, 80, "dilluns", "10:00")]
resultatEsperat = [True, False, False]
for ac, re in zip(activitats, resultatEsperat):
    print("Comment :=>> -------------------------------------------------------")
    print("Comment :=>> Inicialitzant activitat amb els setters amb els valors:")
    print("Comment :=>> Nom: ", ac[0])
    print("Comment :=>> Maxim Participants: ", ac[1])
    print("Comment :=>> Edat Minima: ", ac[2])
    print("Comment :=>> Edat Maxima: ", ac[3])
    print("Comment :=>> Dia: ", ac[4])
    print("Comment :=>> Hora: ", ac[5])
    print("Comment :=>> ---")
    if (not re):
        print("Comment :=>> Resultat esperat: EXCEPCIO")
        print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut despres inicialitzacio:")
    try:
        act = a.Activitat()
        act.nom = ac[0]
        act.maxParticipants = ac[1]
        act.edatMinima = ac[2]
        act.edatMaxima = ac[3]
        act.dia = ac[4]
        act.hora = ac[5]
        resultat = True
        print("Comment :=>> Nom: ", act.nom)
        print("Comment :=>> Maxim Participants: ", act.maxParticipants)
        print("Comment :=>> Edat Minima: ", act.edatMinima)
        print("Comment :=>> Edat Maxima: ", act.edatMaxima)
        print("Comment :=>> Dia: ", act.dia)
        print("Comment :=>> Hora: ", act.hora)
    except AssertionError:
        print("Comment :=>> EXCEPCIO")
        resultat = False
    if (resultat == re):
        if (resultat):
            if (act.nom == ac[0]) and (act.maxParticipants == ac[1]) and (act.edatMinima == ac[2]) and (act.edatMaxima == ac[3]) and (act.dia == ac[4]) and (act.hora == ac[5]):
                print("Comment :=>> CORRECTE")
            else:
                print("Comment :=>> ERROR")
                reduccio = reduccio + 1.0
        else:
            print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ")
print("Comment :=>> Test del metode afegeixParticipant")
print("Comment :=>> ==================================")
reduccio = 0.0
activitat = a.Activitat()
activitat.nom = "activitat_1"
activitat.maxParticipants = 3
activitat.edatMinima = 30
activitat.edatMaxima = 50
activitat.dia = "dilluns"
activitat.hora = "10:00"
print("Comment :=>> ")
print("Comment :=>> -------------------------------------------------------")
print("Comment :=>> Inicialitzant activitat amb aquests valors:")
print("Comment :=>> Nom: ", activitat.nom)
print("Comment :=>> Maxim Participants: ", activitat.maxParticipants)
print("Comment :=>> Edat Minima: ", activitat.edatMinima)
print("Comment :=>> Edat Maxima: ", activitat.edatMaxima)
print("Comment :=>> Dia: ", activitat.dia)
print("Comment :=>> Hora: ", activitat.hora)
usuaris = [("codi_1", "nom_1", 18), ("codi_1", "nom_1", 60), ("codi_1", "nom_1", 40), ("codi_1",
                                                                                       "nom_1", 35), ("codi_2", "nom_2", 40), ("codi_3", "nom_3", 40), ("codi_4", "nom_4", 40)]
resultatEsperat = [False, False, True, False, True, True, False]
nParticipants = [0, 0, 1, 1, 2, 3, 3]
for us, re, np in zip(usuaris, resultatEsperat, nParticipants):
    print("Comment :=>> -------------------------------------------------------")
    print("Comment :=>> Afegint usuari amb dades:")
    print("Comment :=>> Codi: ", us[0])
    print("Comment :=>> Nom: ", us[1])
    print("Comment :=>> Edat: ", us[2])
    print("Comment :=>> ---")
    if (not re):
        print("Comment :=>> Resultat esperat: EXCEPCIO")
    else:
        print("Comment :=>> Numero d'insrits esperats: ", np)
    print("Comment :=>> ---")
    try:
        usr = u.Usuari()
        usr.codi = us[0]
        usr.nom = us[1]
        usr.edat = us[2]
        activitat.afegeixParticipant(usr)
        print("Comment :=>> Numero d'inscrits despres insercio: ",
              activitat.nParticipants())
        resultat = True
    except AssertionError:
        print("Comment :=>> Resultat obtingut: EXCEPCIO")
        resultat = False
    if (resultat == re):
        if (resultat):
            if (activitat.nParticipants() == np):
                print("Comment :=>> CORRECTE")
            else:
                print("Comment :=>> ERROR")
                reduccio = reduccio + 1.0
        else:
            print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
if (reduccio > 5):
    reduccio = 5
grade = grade + (3 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ")
print("Comment :=>> Test del metode buscaParticipant")
print("Comment :=>> ==================================")
reduccio = 0.0
print("Comment :=>> ")
print("Comment :=>> ------------------------------------------------------------------------")
print("Comment :=>> Suposem que s'han afegit els participants del test anterior correctament:")
print("Comment :=>> ------------------------------------------------------------------------")
print("Comment :=>> ")
resultatEsperat = [("codi_1", "nom_1", 40), ("codi_2",
                                             "nom_2", 40), ("codi_3", "nom_3", 40), None, None]
noms = ["nom_1", "nom_2", "nom_3", "nom_4", "nom_5"]
for n, re in zip(noms, resultatEsperat):
    print("Comment :=>> -------------------------------------------------------")
    print("Comment :=>> Nom del participant: ", n)
    print("Comment :=>> ---")
    if (re == None):
        print("Comment :=>> Resultat esperat: ", re)
    else:
        print("Comment :=>> Codi usuari esperat: ", re[0])
        print("Comment :=>> Nom usuari esperat: ", re[1])
        print("Comment :=>> Edat usuari esperada: ", re[2])
    usr = activitat.buscaParticipant(n)
    print("Comment :=>> ---")
    if (usr == None):
        print("Comment :=>> Resultat obtingut: ", usr)
    else:
        print("Comment :=>> Codi usuari obtingut: ", usr.codi)
        print("Comment :=>> Nom usuari obtingut: ", usr.nom)
        print("Comment :=>> Edat usuari obtinguda: ", usr.edat)
    if (re == None):
        if (usr == None):
            print("Comment :=>> CORRECTE")
        else:
            print("Comment :=>> ERROR")
            reduccio = reduccio + 1.0
    else:
        if (usr == None):
            print("Comment :=>> ERROR")
            reduccio = reduccio + 1.0
        else:
            if (usr.codi == re[0]) and (usr.nom == re[1]) and (usr.edat == re[2]):
                print("Comment :=>> CORRECTE")
            else:
                print("Comment :=>> ERROR")
                reduccio = reduccio + 1.0
if (reduccio > 5):
    reduccio = 5
grade = grade + (3 - reduccio)


if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
