from biblioteca import Biblioteca
import datetime as dt


grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")

print ("Comment :=>> Llegint fitxer 'biblioteca.txt' per inicialitzar dades de les publicacions...")
print ("Comment :=>> =============================================================================")
b = Biblioteca()
b.llegeix_publicacions("biblioteca.txt")

print ("Comment :=>> ")
print ("Comment :=>> Test del metode PRESTA  de la classe BIBLIOTECA")
print ("Comment :=>> (Assumeix funcionament correcte de llegeixPublicacions)")
print ("Comment :=>> ======================================================")
reduccio = 0.0
codiUsuari = "USUARI_1";
dataPrestec = dt.date (2018, 1, 1)
codiPublicacio = ["CODI_4", "CODI_4", "CODI_4", "CODI_3", "CODI_3", "CODI_2", "CODI_2", "CODI_5", "CODI_7", "CODI_8"]
codiExemplar = [0, 0, 0, 0, 0, 1, 1, 0, 1, 0]
resultatEsperat = [True, True, False, True, False, True, False, False, False, False]
dataRetornEsperat = [[21, 1, 2018], [21, 1, 2018], [21, 1, 2018], [16, 1, 2018], [16, 1, 2018], 
                     [31, 1, 2018], [31, 1, 2018], [31, 1, 2018], [31, 1, 2018], [31, 1, 2018]]
i = 1
for cp, ce, re, dre in zip(codiPublicacio, codiExemplar, resultatEsperat, dataRetornEsperat):
    dataRetornEsperat = dt.date(dre[2], dre[1], dre[0])
    print ("TEST: ", i)
    i += 1
    print ("Comment :=>> Dades del prestec:")
    print ("Comment :=>> Codi Usuari: ", codiUsuari)
    print ("Comment :=>> Codi Publicacio: ", cp)
    print ("Comment :=>> Data Prestec: ", dataPrestec)
    print ("Comment :=>> Codi Exemplar: ", ce)
    print ("Comment :=>> ----------")
    print ("Comment :=>> Valor retorn esperat", re)
    if re:
        print ("Comment :=>> Data retorn esperat", dataRetornEsperat)
    print ("Comment :=>> ----------")
    correcte, dataRetorn = b.presta(codiUsuari, cp, dataPrestec, ce)
    print ("Comment :=>> Valor retorn obtingut", correcte)
    if correcte:
        print ("Comment :=>> Data retorn obtinguda", dataRetorn)
    if correcte == re:
        if correcte:
            if dataRetorn == dataRetornEsperat:
                print ("Comment :=>> CORRECTE")
            else:
                print ("Comment :=>> ERROR")
                reduccio = reduccio + 1.0
        else:
            print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    print ("Comment :=>> -------------------------------------------------------")
if (reduccio > 8):
    reduccio = 8
grade = grade + (5 - reduccio)
print ("Grade :=>>", grade)

print ("Comment :=>> ")
print ("Comment :=>> Test del metode RETORNA  de la classe BIBLIOTECA")
print ("Comment :=>> (Assumeix funcionament correcte de PRESTAR)")
print ("Comment :=>> ================================================")
reduccio = 0.0
codiUsuari = ["USUARI_1", "USUARI_1", "USUARI_1", "USUARI_1", "USUARI_1", "USUARI_1", "USUARI_1", "USUARI_1", "USUARI_1", "USUARI_2"]
codiPublicacio = ["CODI_4", "CODI_4", "CODI_4", "CODI_6", "CODI_2", "CODI_2", "CODI_2", "CODI_7", "CODI_8", "CODI_3"]
dataRetorn = [
		[ 20, 1, 2018 ],
		[ 22, 1, 2018 ],
		[ 20, 1, 2018 ],
		[ 1, 1, 2018 ],
		[ 1, 2, 2018 ],
		[ 1, 2, 2018 ],
		[ 1, 2, 2018 ],
		[ 1, 2, 2018 ],
		[ 1, 2, 2018 ],
		[ 1, 2, 2018 ]
	];
codiExemplar = [ 0, 0, 0, 0, 1, 1, 2, 1, 0, 0 ]
resultatEsperat = [ True, True, False, False, True, False, False, False, False, False ]
dataCorrectaEsperada =	[ True, False, True, True, False, False, False, False, False, False	]
i = 1
for cu, cp, dr, ce, re, dce in zip(codiUsuari, codiPublicacio, dataRetorn, codiExemplar, resultatEsperat, dataCorrectaEsperada):
    drDate = dt.date(dr[2], dr[1], dr[0])
    print ("TEST: ", i)
    i += 1
    print ("Comment :=>> Dades de la devolucio:")
    print ("Comment :=>> Codi Usuari: ", cu)
    print ("Comment :=>> Codi Publicacio: ", cp)
    print ("Comment :=>> Data Retorn: ", drDate)
    print ("Comment :=>> Codi Exemplar: ", ce)
    print ("Comment :=>> ----------")
    print ("Comment :=>> Valor retorn esperat", re)
    if re:
        print ("Comment :=>> Data correcta esperada", dce)
    print ("Comment :=>> ----------")
    correcte, dataCorrecta = b.retorna(cu, cp, ce, drDate)
    print ("Comment :=>> Valor retorn obtingut", correcte)
    if correcte:
        print ("Comment :=>> Data correcta obtinguda", dataCorrecta)
    if correcte == re:
        if correcte:
            if dataCorrecta == dce:
                print ("Comment :=>> CORRECTE")
            else:
                print ("Comment :=>> ERROR")
                reduccio = reduccio + 1.0
        else:
            print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    print ("Comment :=>> -------------------------------------------------------")
if (reduccio > 8):
    reduccio = 8
grade = grade + (5 - reduccio)

if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)
print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
