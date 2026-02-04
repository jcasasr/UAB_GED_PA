import exercici

grade = 0
print("Grade :=>>", grade)


print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>>")

reduccio = 0
print("Comment :=>> ")
print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio elimina_duplicats")
llista = [[1, 2, 3, 4], [], [4, 4, 4, 4], [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]]
noDuplicatsEsperat = [[1, 2, 3, 4], [], [4], [5, 4, 3, 2, 1]]
for i, l in enumerate(llista):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i+1)
    print("Comment :=>> Llista Original: ", l)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", noDuplicatsEsperat[i])
    resultat = exercici.elimina_duplicats(l)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == noDuplicatsEsperat[i]):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.5
if (reduccio > 10.0):
    reduccio = 10.0
grade = grade + (10.0 - reduccio)
if (grade < 0):
    grade = 0
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
