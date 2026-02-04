import exercici

grade = 0
print("Grade :=>>", grade)


print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>>")

reduccio = 0
print("Comment :=>> ")
print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio binari_decimal")
binari = [[1, 1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0],
          [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1],
          [0, 0, 1, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0, 1, 1]]
decimalEsperat = [-1, 0, -6, 6, -86, 85, 42, -117]
for i, b in enumerate(binari):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i+1)
    print("Comment :=>> Numero binari: ", b)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", decimalEsperat[i])
    resultat = exercici.binari_decimal(b)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == decimalEsperat[i]):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 10.0):
    reduccio = 10.0
grade = grade + (10.0 - reduccio)
if (grade < 0):
    grade = 0
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
