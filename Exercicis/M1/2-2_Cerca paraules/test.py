import exercici


diccionari_esperat = {'python': [[0, 1]],
 'is': [[0, 2]],
 'an': [[0, 1], [1, 1]],
 'easy': [[0, 1]],
 'to': [[0, 1], [3, 1]],
 'learn': [[0, 1]],
 'powerful': [[0, 1]],
 'programming': [[0, 1], [4, 1]],
 'language': [[0, 1], [1, 1]],
 'it': [[0, 1], [2, 1]],
 'ideal': [[1, 1]],
 'for': [[1, 1]],
 'scripting': [[1, 1]],
 'and': [[1, 1], [3, 1]],
 'rapid': [[1, 1]],
 'application': [[1, 1]],
 'development': [[1, 1]],
 'in': [[2, 1]],
 'many': [[2, 1]],
 'areas': [[2, 1]],
 'on': [[2, 1]],
 'most': [[2, 1]],
 'platforms': [[2, 1]],
 'has': [[2, 1]],
 'efficient': [[2, 1]],
 'high-level': [[2, 1]],
 'data': [[3, 1]],
 'structures': [[3, 1]],
 'a': [[3, 1]],
 'simple': [[3, 1]],
 'but': [[3, 1]],
 'effective': [[3, 1]],
 'approach': [[3, 1]],
 'object-oriented': [[4, 1]]}

grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio indexParaules" )
diccionari_obtingut = exercici.index_paraules('fitxerParaules.txt')
reduccio = 0
for paraula, valor in sorted(diccionari_esperat.items()):
    print ("Comment :=>> ------------------------------------------")
    print ("Comment :=>> Paraula: ", paraula)
    print ("Comment :=>> Resultat esperat: ", valor)       
    print ("Comment :=>> ---")
    if (paraula in diccionari_obtingut):
        print ("Comment :=>> Resultat obtingut: ", diccionari_obtingut[paraula])       
        if (valor == diccionari_obtingut[paraula]):    
            print ("Comment :=>> CORRECTE")
        else:
            print ("Comment :=>> ERROR")
            reduccio = reduccio + 1.0
    else:
        print ("Comment :=>> ERROR. La paraula no esta al diccionari")
        reduccio = reduccio + 1.0        
correcte = False
if (len(diccionari_esperat) == len(diccionari_obtingut)):
    correcte = True
    for paraula in diccionari_obtingut.keys():
        if paraula not in diccionari_esperat:
            correcte = False
            break
if (correcte):    
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR. No hi ha les mateixes paraules al diccionari")
    reduccio = reduccio + 2.0

if (reduccio > 8):
    reduccio = 8
grade = grade + (6.0 - reduccio)
print ("Grade :=>>", grade)


paraules_cerca = ['python', 'it', 'an', 'is', 'program']
resultat_esperat = [[['Python is an easy to learn, powerful programming language. It is', 1]],
                   [['Python is an easy to learn, powerful programming language. It is', 1],
                    ['in many areas on most platforms. It has efficient high-level', 1]],
                   [['Python is an easy to learn, powerful programming language. It is', 1],
                    ['an ideal language for scripting and rapid application development', 1]],
                    [['Python is an easy to learn, powerful programming language. It is', 2]],
                    []]
reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> =======================================")
print ("Comment :=>> Test del metode cercaParaula" )
i = 1
reduccio = 0
for paraula, resultat in zip(paraules_cerca, resultat_esperat):
    print ("Comment :=>> ------------------------------------------")
    print ("Comment :=>> Test: ", i)
    print ("Comment :=>> Paraula a cercar: ", paraula)
    resultat_obtingut = exercici.cerca_paraula(paraula, diccionari_esperat, 'fitxerParaules.txt')
    if resultat == []:
        print ("Comment :=>> La paraula no esta al fitxer. Resultat Esperat:", [] )
        print ("Comment :=>> ---")
        print ("Comment :=>> Resultat obtingut: ", resultat_obtingut)
        if resultat == resultat_obtingut:
            print ("Comment :=>> CORRECTE")
        else:
            print ("Comment :=>> ERROR")
            reduccio = reduccio + 1.0            
    else:
        for index, valor in enumerate(resultat):
            print ("Comment :=>> ---")
            print ("Comment :=>> Linia Esperada: ", valor[0])
            print ("Comment :=>> Nº repeticions esperat: ", valor[1])
            print ("Comment :=>> ---")
            if (index < len(resultat_obtingut)):
                resultat_obtingut[index][0] = resultat_obtingut[index][0].replace('\n','')
                resultat_obtingut[index][0] = resultat_obtingut[index][0].strip()
                print ("Comment :=>> Linia Obtinguda: ", resultat_obtingut[index][0])
                print ("Comment :=>> Nº repeticions obtingut: ", resultat_obtingut[index][1])
                if (valor == resultat_obtingut[index]):
                    print ("Comment :=>> CORRECTE")
                else:
                    print ("Comment :=>> ERROR")
                    reduccio = reduccio + 1.0
            else:
                print ("Comment :=>> ERROR. S'han recuperat menys linies de les esperades")
                reduccio = reduccio + 2.0
        if (len(resultat_obtingut) > len(resultat)):
            print ("Comment :=>> ERROR. S'han recuperat mes linies de les esperades")
            reduccio = reduccio + 2.0
    i = i + 1


if (reduccio > 5):
    reduccio = 5
grade = grade + (4.0 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
