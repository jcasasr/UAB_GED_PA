import mastermind as m
import sys


sys.stdin = open("test.txt", 'r')

grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

n_partides = 4
n_valors = [5, 5, 5, 4]
max_intents = [10, 10, 10, 5]
combinacions = ['VVVVV', 'BVERT', 'VBEBB', 'VBVB']
resultat_esperat = [
    ['ERROR', 'ERROR', [1], [], [1], [1], [1], [1, 1, 1, 1, 1]],
    [[0, 0], [1, 0, 0], [0, 0, 0], [0], [0, 0, 0], [0, 0, 0], [
        0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0]],
    [[1, 1, 0], [1], [0, 0], [0], [1, 0, 0, 0], [0, 0, 0], [
        1, 0, 0, 0], [0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]],
    ['ERROR', [], [1, 1], [], [1, 1, 1], [1, 1, 0, 0]]
]
final_esperat = [True, False, True, False]

colors_disponibles = {'V': 'Vermell', 'B': 'Blau', 'T': 'Taronja', 'R': 'Rosa',
                      'E': 'vErd', 'M': 'Marro', 'G': 'Groc', 'N': 'Negre'
                      }


for i in range(n_partides):
    reduccio = 0
    print("Comment :=>> --------------------")
    print("Comment :=>> Iniciant PARTIDA", i+1)
    print("Comment :=>> Nº valors combinacio: ", n_valors[i])
    print("Comment :=>> Màxim intents: ", max_intents[i])
    print("Comment :=>> --------------------")
    print("Comment :=>> ")
    codi = m.Codi(n_valors[i], list(combinacions[i]))
    endevinat, llista_combinacions = m.mastermind(
        n_valors[i], max_intents[i], codi, colors_disponibles)

    print("Comment :=>> Codi secret a endevinar: ", combinacions[i])
    print("Comment :=>> ")
    for c, re in zip(llista_combinacions, resultat_esperat[i]):
        print("Comment :=>> --------------")
        print("Comment :=>> Combinacio introduïda: ", c.get_combinacio())
        print("Comment :=>> ---")
        print("Comment :=>> Resultat esperat: ", re)
        print("Comment :=>> ---")
        if (re == 'ERROR'):
            if c.get_correcte():
                print("Comment :=>> Resultat obtingut: ", c.get_resultat())
                print("Comment :=>> ERROR")
                reduccio = reduccio + 1.0
            else:
                print("Comment :=>> Resultat obtingut: ERROR")
                print("Comment :=>> CORRECTE")
        else:
            if not c.get_correcte():
                print("Comment :=>> Resultat obtingut: ERROR")
                print("Comment :=>> ERROR")
                reduccio = reduccio + 1.0
            else:
                print("Comment :=>> Resultat obtingut: ", c.get_resultat())
                if (c.get_resultat() == re):
                    print("Comment :=>> CORRECTE")
                else:
                    print("Comment :=>> ERROR")
                    reduccio = reduccio + 1.0
    print("Comment :=>> --------------")
    print("Comment :=>> Resultat final de la partida esperat: ",
          final_esperat[i])
    print("Comment :=>> ---")
    print("Comment :=>> Resultat final de la partida obtingut: ", endevinat)
    if (endevinat == final_esperat[i]):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0

    salt_partida = input()

    if (reduccio > 5):
        reduccio = 5
    grade = grade + (2.5 - reduccio)
    print("Grade :=>>", grade)


if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")

sys.stdin = sys.__stdin__
