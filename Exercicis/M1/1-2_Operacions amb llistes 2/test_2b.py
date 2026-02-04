import exercici

grade = 0
print("Grade :=>>", grade)


print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>>")

reduccio = 0
print("Comment :=>> ")
print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio unio")
llista1 = [[1, 2, 3, 4], [1, 2], [], [1, 2], [4, 3, 2, 1]]
llista2 = [[0, 2, 3, 5], [1, 2], [1, 2], [], [5, 6]]
llistaEsperada = [[1, 2, 3, 4, 0, 5], [1, 2], [1, 2], [1, 2],
                  [4, 3, 2, 1, 5, 6]]
i = 1
for l1, l2, le in zip(llista1, llista2, llistaEsperada):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", le)
    resultat = exercici.unio(l1, l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == le):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    i = i + 1
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2 - reduccio)
if (grade < 0):
    grade = 0
print("Grade :=>> ", grade)


reduccio = 0
print("Comment :=>> ")
print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio multiplicacio_llistes")
llista1 = [[1, 2, 3, 4], [1, 2], [2], [1, 2], [4, 3, 2, 1]]
llista2 = [[0, 2, 3, 5], [1], [1, 2], [], [5, 6]]
llistaEsperada = [[0, 4, 9, 20], [1], [2], [], [20, 18]]
i = 1
for l1, l2, le in zip(llista1, llista2, llistaEsperada):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", le)
    resultat = exercici.multiplicacio_llistes(l1, l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == le):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    i = i + 1
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2 - reduccio)
if (grade < 0):
    grade = 0
print("Grade :=>> ", grade)

print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
