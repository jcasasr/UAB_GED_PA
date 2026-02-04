import exercici

grade = 0
print("Grade :=>>", grade)


print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>>")

reduccio = 0
print("Comment :=>> ")
print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio distancia_hamming")
llista1 = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0],
           [0, 0, 0, 0]]
llista2 = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1],
           [1, 0, 0, 0]]
distancia_esperada = [0, 0, 4, 2, 1]
i = 1
for l1, l2, de in zip(llista1, llista2, distancia_esperada):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", de)
    resultat = exercici.distancia_hamming(l1, l2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ", resultat)
    if (resultat == de):
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
