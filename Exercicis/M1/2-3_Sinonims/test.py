import exercici


diccionari = dict()
diccionari['feta'] = ['realitzada', 'produida', 'elaborada']
diccionari['content'] = ['encantat', 'satisfet', 'cofoi']
diccionari['molt'] = ['força']
diccionari['feina'] = ['tasca', 'ocupacio']

grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>>")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio afegeixSinonim" )
diccionari_obtingut = dict()
for paraula, sinonims in diccionari.items():
    print ("Comment :=>> Afegint sinonims de:", paraula, "-->", sinonims)
    for sinonim in sinonims:
        exercici.afegeix_sinonim(diccionari_obtingut, paraula, sinonim)
print ("Comment :=>> Afegint sinonims de:", 'content', "-->", 'cofoi')
exercici.afegeix_sinonim(diccionari_obtingut, 'content', 'cofoi')
print ("Comment :=>> Afegint sinonims de:", 'feta', "-->", 'realitzada')
exercici.afegeix_sinonim(diccionari_obtingut, 'feta', 'realitzada')
print ("Comment :=>> Afegint sinonims de:", 'molt', "-->", 'força')
exercici.afegeix_sinonim(diccionari_obtingut, 'molt', 'força')

reduccio = 0
print ("Comment :=>> -----------------------------")
print ("Comment :=>> Comprovant diccionari obtingut......")
for paraula, sinonims in diccionari.items():
    print ("Comment :=>> -----------------------------")    
    print ("Comment :=>> Paraula esperada: ", paraula)
    print ("Comment :=>> Sinonims esperats: ", sinonims)
    print ("Comment :=>> ----")
    print ("Comment :=>> Sinonims obtinguts: ", diccionari_obtingut[paraula])
    correcte = False
    if (len(diccionari_obtingut[paraula]) == len(sinonims)):
        correcte = True
        for sinonim in diccionari_obtingut[paraula]:
            if sinonim not in sinonims:
                correcte = False
                break
    if (correcte):    
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 2.0

correcte = False
if (len(diccionari) == len(diccionari_obtingut)):
    correcte = True
    for paraula in diccionari_obtingut.keys():
        if paraula not in diccionari:
            correcte = False
            break
if (correcte):    
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR. No hi ha les mateixes paraules al diccionari")
    reduccio = reduccio + 2.0

if (reduccio > 6.0):
    reduccio = 6.0
grade = grade + (5.0 - reduccio)
print ("Grade :=>>", grade)


reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> =======================================")
print ("Comment :=>> Test del metode conversioSinonims" )
frase = ['està', 'molt', 'content', 'de', 'la', 'feina', 'feta']
print ("Comment :=>> Frase original: ", frase)
frase_esperada = ['està', 'força', ['encantat', 'satisfet', 'cofoi'], 'de', 'la', ['tasca', 'ocupacio'], ['realitzada', 'produida', 'elaborada']]
print ("Comment :=>> ---")
print ("Comment :=>> Resultat esperat (pot ser qualsevol sinonim de cada llista): ", frase_esperada)
print ("Comment :=>> ---")
nova_frase = exercici.conversio_sinonims(frase, diccionari_obtingut)
print ("Comment :=>> Resultat obtingut: ", nova_frase)
correcte = False
if (len(frase_esperada) == len(nova_frase)):
    correcte = True
    for sinonim_esperat, sinonim_obtingut in zip(frase_esperada, nova_frase):
        if (type(sinonim_esperat) == str):
            if (sinonim_esperat != sinonim_obtingut):
                correcte = False
                break
        if (type(sinonim_esperat) == list):
            if (sinonim_obtingut not in sinonim_esperat):
                correcte = False
                break  
if (correcte):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = 6.0
grade = grade + (5.0 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
