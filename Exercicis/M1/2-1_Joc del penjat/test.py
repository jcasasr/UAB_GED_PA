import penjat as p
import sys

grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

n_partides = 2
max_errors = [10, 10]
paraules = ['python', 'python']
resultat_esperat = [['----o-', 'p---o-', 'p---o-', 'p---on', 'p---on', 'ERROR', 'p-t-on', 'pyt-on', 'python'],
                    ['------', '------', '------', '------', '------', '------', '------', '---h--', '---h--', '---h--',
                     '---h--']]

final_esperat = [True, False]

for i in range(n_partides):
    reduccio = 0
    print("Comment :=>> --------------------")
    print("Comment :=>> Iniciant PARTIDA", i + 1)
    print("Comment :=>> Paraula a endevianr: ", paraules[i])
    print("Comment :=>> Màxim errors permesos: ", max_errors[i])
    print("Comment :=>> --------------------")
    print("Comment :=>> ")

    sys.stdin = open("test" + str(i + 1) + ".txt", 'r')
    endevinat, lletres, resultat = p.juga_penjat(paraules[i], max_errors[i])
    sys.stdin = sys.__stdin__

    print("Comment :=>> ")
    for l, r, re in zip(lletres, resultat, resultat_esperat[i]):
        print("Comment :=>> --------------")
        print("Comment :=>> Lletra introduïda: ", l)
        print("Comment :=>> ---")
        print("Comment :=>> Resultat esperat: ", re)
        print("Comment :=>> ---")
        print("Comment :=>> Resultat obtingut: ", r)
        if (r == re):
            print("Comment :=>> CORRECTE")
        else:
            print("Comment :=>> ERROR")
            reduccio = reduccio + 1.0
    print("Comment :=>> --------------")
    print("Comment :=>> Resultat final de la partida esperat: ", final_esperat[i])
    print("Comment :=>> ---")
    print("Comment :=>> Resultat final de la partida obtingut: ", endevinat)
    if (endevinat == final_esperat[i]):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0

    if (reduccio > 8):
        reduccio = 8
    grade = grade + (5 - reduccio)
    print("Grade :=>>", grade)

if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
