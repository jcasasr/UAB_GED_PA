import exercici

diccionari_esperat = {'p': [3, ['python', 'powerful', 'programming']],
 'y': [2, ['python', 'easy']],
 't': [3, ['python', 'to', 'object-oriented']],
 'h': [1, ['python']],
 'o': [5, ['python', 'to', 'powerful', 'object-oriented', 'programming']],
 'n': [6, ['python', 'an', 'learn', 'object-oriented', 'programming', 'language']],
 'i': [3, ['is', 'object-oriented', 'programming']],
 's': [2, ['is', 'easy']],
 'a': [5, ['an', 'easy', 'learn', 'programming', 'language']],
 'e': [5, ['easy', 'learn', 'powerful', 'object-oriented', 'language']],
 'l': [3, ['learn', 'powerful', 'language']],
 'r': [4, ['learn', 'powerful', 'object-oriented', 'programming']],
 'w': [1, ['powerful']],
 'f': [1, ['powerful']],
 'u': [2, ['powerful', 'language']],
 'b': [1, ['object-oriented']],
 'j': [1, ['object-oriented']],
 'c': [1, ['object-oriented']],
 'd': [1, ['object-oriented']],
 'g': [2, ['programming', 'language']],
 'm': [1, ['programming']]}

grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio indexCaracter" )
diccionari_obtingut = exercici.index_caracter('fitxerParaules.txt')
reduccio = 0
for caracter, valor in sorted(diccionari_esperat.items()):
    print ("Comment :=>> ------------------------------------------")
    print ("Comment :=>> Caracter: ", caracter)
    print ("Comment :=>> Resultat esperat: ", valor)       
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut: ", diccionari_obtingut[caracter])       
    if (valor == diccionari_obtingut[caracter]):    
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
if (len(diccionari_obtingut) > len(diccionari_esperat)):
    print ("Comment :=>> ------------------------------------------")
    print ("Comment :=>> ERROR. Al diccionari hi ha més entrades de les esperades")
    reduccio = reduccio + 1.0

if (reduccio > 8):
    reduccio = 8
grade = grade + (6.0 - reduccio)
print ("Grade :=>>", grade)


resultat_esperat = [['a', 'programming'],
 ['b', 'object-oriented'],
 ['c', 'object-oriented'],
 ['d', 'object-oriented'],
 ['e', 'object-oriented'],
 ['f', 'powerful'],
 ['g', 'programming'],
 ['h', 'python'],
 ['i', 'object-oriented'],
 ['j', 'object-oriented'],
 ['l', 'powerful'],
 ['m', 'programming'],
 ['n', 'object-oriented'],
 ['o', 'object-oriented'],
 ['p', 'programming'],
 ['r', 'object-oriented'],
 ['s', 'easy'],
 ['t', 'object-oriented'],
 ['u', 'powerful'],
 ['w', 'powerful'],
 ['y', 'python']]
reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> =======================================")
print ("Comment :=>> Test del metode maxParaulaCaracter" )
resultat_obtingut = exercici.max_paraula_caracter(diccionari_esperat)
reduccio = 0
for index, valor in enumerate(resultat_esperat):
    print ("Comment :=>> ------------------------------------------")
    print ("Comment :=>> Caracter Esperat: ", valor[0])
    print ("Comment :=>> Paraula mes llarga esperada: ", valor[1])       
    print ("Comment :=>> ---")
    if (index < len(resultat_obtingut)):
        print ("Comment :=>> Caracter obtingut: ", resultat_obtingut[index][0])       
        print ("Comment :=>> Paraula mes llarga obtinguda: ", resultat_obtingut[index][1])       
        if (valor == resultat_obtingut[index]):    
            print ("Comment :=>> CORRECTE")
        else:
            print ("Comment :=>> ERROR")
            reduccio = reduccio + 1.0
    else:
        print ("Comment :=>> ERROR. Al resultat hi ha menys valors dels esperats")
        reduccio = reduccio + 1.0
        
if (len(resultat_obtingut) > len(resultat_esperat)):
    print ("Comment :=>> ------------------------------------------")
    print ("Comment :=>> ERROR. Al resultat hi ha mes valors dels esperats")
    reduccio = reduccio + 1.0

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
