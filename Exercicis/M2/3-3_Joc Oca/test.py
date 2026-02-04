import joc


grade = 0
print ("Grade :=>>", grade)

valors_dau = [ 2, 2, 5, 4, 3, 2, 3, 1, 2, 1, 2, 1, 2, 1 ]

print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>> ")

print ("Grade :=>>", grade)

print ("Comment :=>> Jugant partida cridant a la funció joc_oca")
print ("Comment :=>> Partida amb 3 jugadors i les caselles del fitxer oca.txt")
print ("Comment :=>> Els valors del dau per cadascun dels torns són: ")
print ("Comment :=>>", valors_dau)
print ("Comment :=>> ===============================================================")

guanyador, resultat = joc.joc_oca("oca.txt", 3, valors_dau)

resultat_esperat = [
        (1, True, 5),
        (1, True, 7),
        (2, True, 6),
        (3, True, 10),
        (3, True, 10),
        (1, False, 7),
        (2, True, 1),
        (3, True, 11),
        (1, False, 7),
        (2, True, 2),
        (3, True, 11),
        (1, True, 8),
        (2, True, 4),
        (3, True, 12)
        ]
guanyador_esperat = 3

print ("Comment :=>> ")
print ("Comprovant el resultat de la partida")
print ("Comment :=>> ----------------------------------------------------------------")

n_torn = 1
reduccio = 0.0
for vd, re, ro in zip(valors_dau, resultat_esperat, resultat):
    print ("Comment :=>> Torn: ", n_torn)
    print ("Comment :=>> Valor del dau: ", vd)
    print ("Comment :=>> ---")
    print ("Comment :=>> Valors esperats (n. jugador, pot tirar, posicio): ", re)
    print ("Comment :=>> ---")
    print ("Comment :=>> Valors obtinguts (n. jugador, pot tirar, posicio): ", ro)
    if re == ro:    
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    print ("Comment :=>> ----------------------------------------------")
    n_torn += 1
print ("Comment :=>> Guanyador esperat: ", guanyador_esperat)
print ("Comment :=>> ---")
print ("Comment :=>> Guanyador obtingut: ", guanyador)
if guanyador_esperat == guanyador:    
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0

if (reduccio > 10):
    reduccio = 10
grade = grade + (10 - reduccio)

if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)
print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
