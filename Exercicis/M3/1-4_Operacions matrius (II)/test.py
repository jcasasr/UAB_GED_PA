import exercici
import numpy as np


def mostra_matriu(matriu):
    for fila in matriu:
        print("Comment :=>> ", fila)


grade = 0
print("Grade :=>>", grade)


print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")
print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio canviaValorForaRang")
matriu = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Comment :=>> ")
print("Comment :=>> Matriu: ")
mostra_matriu(matriu)

rangValors = [[3, 5], [6, 6], [-1, 3], [7, 15], [10, 12]]
nouValor = 0

resultatEsperat = [np.array([[0, 0, 3], [4, 5, 0], [0, 0, 0]]),
                   np.array([[0, 0, 0], [0, 0, 6], [0, 0, 0]]),
                   np.array([[1, 2, 3], [0, 0, 0], [0, 0, 0]]),
                   np.array([[0, 0, 0], [0, 0, 0], [7, 8, 9]]),
                   np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])]


reduccio = 0
for matriuEsperada, rang in zip(resultatEsperat, rangValors):
    matriu = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Rang de valors: ", rang)
    print("Comment :=>> Valor de substitucio: ", nouValor)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ")
    mostra_matriu(matriuEsperada)
    matriuResultat = exercici.canvia_valor_fora_rang(
        matriu, rang[0], rang[1], nouValor)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ")
    mostra_matriu(matriuResultat)
    if (matriuResultat == matriuEsperada).all():
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0


if (reduccio > 4):
    reduccio = 4
grade = grade + (2.0 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio sumaNoDiagonal")
matriuOriginal = [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  np.array([[1, 0, 0], [0, 5, 0], [0, 0, 9]]),
                  np.array([[1, -2, -3], [-4, 5, -6], [-7, -8, 9]])]
sumaEsperada = [30, 0, -30]
reduccio = 0
for m, s in zip(matriuOriginal, sumaEsperada):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Matriu: ")
    mostra_matriu(m)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", s)
    sumaObtinguda = exercici.suma_no_diagonal(m)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ", sumaObtinguda)
    if (sumaObtinguda == s):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.0 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio diagonalDominant")
matriuOriginal = [np.array([[10, 2, 3], [4, 50, 6], [7, 8, 90]]),
                  np.array([[10, 0, 0], [10, 5, 0], [10, 0, 9]]),
                  np.array([[10, 5, 0], [10, 5, 0], [0, 0, 9]])]
valorEsperat = [True, False, False]
reduccio = 0
for m, v in zip(matriuOriginal, valorEsperat):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Matriu: ")
    mostra_matriu(m)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", v)
    resultat = exercici.diagonal_dominant(m)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ", resultat)
    if (resultat == v):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.0 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio maxFila")
matriuOriginal = [np.array([[10, 2, 3], [4, 50, 6], [7, 8, 90]]),
                  np.array([[10, 0, 0], [10, 5, 0], [10, 0, 9]]),
                  np.array([[10, 5, 0], [10, 5, 0], [0, 0, 9]])]
valorEsperat = [[(10, 0), (50, 1), (90, 2)],
                [(10, 0), (10, 0), (10, 0)],
                [(10, 0), (10, 0), (9, 2)]]
reduccio = 0
for m, v in zip(matriuOriginal, valorEsperat):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Matriu: ")
    mostra_matriu(m)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", v)
    resultat = exercici.max_fila(m)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ", resultat)
    if (resultat == v):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.0 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio maxFila")
matriuOriginal = [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])]
filesIntercanviar = [(0, 1), (1, 1), (2, 1)]
matriuEsperada = [np.array([[4, 5, 6], [1, 2, 3], [7, 8, 9]]),
                  np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  np.array([[1, 2, 3], [7, 8, 9], [4, 5, 6]])]
reduccio = 0
for mo, fi, me in zip(matriuOriginal, filesIntercanviar, matriuEsperada):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Matriu Original: ")
    mostra_matriu(mo)
    print("Comment :=>> Files a intercanviar: ", fi[0], fi[1])
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ")
    mostra_matriu(me)
    resultat = exercici.intercanvi_files(mo, fi[0], fi[1])
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ")
    mostra_matriu(resultat)
    if (resultat == me).all():
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.0 - reduccio)
print("Grade :=>>", grade)


if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
