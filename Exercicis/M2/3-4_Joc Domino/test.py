import domino as d


grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

n_partides = 2
resultat_esperat = [
    [(0, 0), (-1, -1), (-1, -1), (-1, -1), (0, 1), (1, 1), (-1, -1), (-1, -1), (0, 2), (1, 2), (2, 3), (3, 6), (0, 6), (2, 2),
     (2, 4), (4, 4), (0, 3), (1, 3), (3, 4), (-1, -1), (-1, -1), (1, 4), (3, 3), (4, 5), (0, 5), (-1, -1), (3, 5), (5, 5), (0, 4)],
    [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (2, 3), (0, 3), (0, 4),
     (2, 6), (0, 6), (2, 4), (2, 5), (0, 5), (-1, -1), (-1, -1), (-1, -1), (-1, -1)]
]

final_esperat = [1, -1]

fitxes = []
for i in range(7):
    for j in range(i, 7):
        fitxes.append((i, j))

fitxes_inicials = []
fitxes_inicials.append(fitxes)

fitxes_inicials.append([])
for jugador in range(4):
    for j in range(7):
        fitxes_inicials[1].append(fitxes[(j*4) + jugador])

for i in range(n_partides):
    reduccio = 0
    print("Comment :=>> --------------------")
    print("Comment :=>> Iniciant test PARTIDA", i+1)
    print("Comment :=>> Fitxes Inicials: ", fitxes_inicials[i])
    print("Comment :=>> --------------------")
    print("Comment :=>> ")
    print("Comment :=>> Jugant la partida...")
    guanyador, fitxes_jugades = d.juga_domino(fitxes_inicials[i])

    print("Comment :=>> --------------------")
    print("Comment :=>> Jugador guanyador esperat: ", final_esperat[i])
    print("Comment :=>> ---")
    print("Comment :=>> Jugador guanyador obtingut: ", guanyador)
    if (guanyador == final_esperat[i]):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.5
    print("Comment :=>> --------------------")
    print("Comment :=>> Fitxes jugades esperades: ", resultat_esperat[i])
    print("Comment :=>> ---")
    print("Comment :=>> Fitxes jugades obtingudes: ", fitxes_jugades)

    if (len(resultat_esperat[i]) == len(fitxes_jugades)):
        igual = True
        for fj, re in zip(fitxes_jugades, resultat_esperat[i]):
            if not (((fj[0] == re[0]) and (fj[1] == re[1])) or ((fj[0] == re[1]) and (fj[1] == re[0]))):
                igual = False
        if igual:
            print("Comment :=>> CORRECTE")
        else:
            print("Comment :=>> ERROR")
            reduccio = reduccio + 2.5
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.5
    print("Comment :=>> --------------")

    grade = grade + (5.0 - reduccio)
    print("Grade :=>>", grade)

    print("Comment :=>> --------------")

if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
