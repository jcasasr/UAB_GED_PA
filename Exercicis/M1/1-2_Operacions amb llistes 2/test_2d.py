import exercici

grade = 0
print("Grade :=>>", grade)


print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>>")

reduccio = 0
print("Comment :=>> ")
print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio multiplicacio_elements")
llista1 = [[1, 2, 3, 4], [1, 2], [2], [1, 2], [4, 3, 2, 1]]
llista2 = [[0, 2, 3, 5], [1], [1, 2], [], [5, 6]]
llistaEsperada = [[[0, 2, 3, 5], [0, 4, 6, 10], [0, 6, 9, 15], [0, 8, 12, 20]],
                  [[1], [2]], [[2, 4]], [[], []],
                  [[20, 24], [15, 18], [10, 12], [5, 6]]]
i = 1
for l1, l2, le in zip(llista1, llista2, llistaEsperada):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ")
    for x in le:
        print(x)
    resultat = exercici.multiplicacio_elements(l1, l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ")
    for x in resultat:
        print(x)
    if (resultat == le):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
    i = i + 1
if (reduccio > 10.0):
    reduccio = 10.0
grade = grade + (10 - reduccio)
if (grade < 0):
    grade = 0

print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
