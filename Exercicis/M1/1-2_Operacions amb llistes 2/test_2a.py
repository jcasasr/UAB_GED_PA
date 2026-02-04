import exercici

grade = 0
print("Grade :=>>", grade)


print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>>")

reduccio = 0
print("Comment :=>> ")
print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio interseccio")
llista1 = [[1, 2, 3, 4], [1, 2], [], [1, 2], [4, 3, 2, 1]]
llista2 = [[2, 3, 5], [1, 2], [1, 2], [], [5, 6]]
llistaEsperada = [[2, 3], [1, 2], [], [], []]
i = 1
for l1, l2, le in zip(llista1, llista2, llistaEsperada):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", le)
    resultat = exercici.interseccio(l1, l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == le):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
    i = i+1
if (reduccio > 10.0):
    reduccio = 10.0
grade = grade + (10 - reduccio)
if (grade < 0):
    grade = 0

print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
