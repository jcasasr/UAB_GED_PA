import data
import llibre

grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

print("Comment :=>> ========================================================")
print("Comment :=>> Classe Data: Test del mètode es_valida")
dates = [[29, 2, 1996], [29, 2, 1900], [0, 1, 2000], [31, 12, 1997],
         [1, 1, 2004], [31, 4, 1997], [30, 4, 2003], [0, 3, 1703]]
resultat_esperat = [True, False, False, True, True, False, True, False]

reduccio = 0
for d, re in zip(dates, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    dia = data.Data(d[0], d[1], d[2])
    print("Comment :=>> Data: ", dia)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", re)
    resultat = dia.es_valida()
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ", resultat)
    if (re == resultat):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> Classe Data: Test del metode __le__")
dates1 = [[1, 1, 1996], [1, 1, 1900], [2, 1, 1900], [1, 1, 2000],
          [31, 12, 1999], [1, 1, 1997], [1, 2, 1997], [1, 1, 2006],
          [1, 1, 2004]]
dates2 = [[1, 1, 1996], [2, 1, 1900], [1, 1, 1900], [31, 12, 1999],
          [1, 1, 2000], [1, 2, 1997], [1, 1, 1997], [1, 1, 2004], [1, 1, 2006]]
resultat_esperat = [False, True, False, False, True, True, False, False, True]

reduccio = 0
for d1, d2, re in zip(dates1, dates2, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    dia1 = data.Data(d1[0], d1[1], d1[2])
    dia2 = data.Data(d2[0], d2[1], d2[2])
    print("Comment :=>> Data 1: ", dia1)
    print("Comment :=>> Data 2: ", dia2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", re)
    resultat = (dia1 < dia2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ", resultat)
    if (re == resultat):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> Classe Data: Test del metode __eq__")
dates1 = [[1, 1, 1996], [1, 1, 1900], [1, 1, 2000], [1, 1, 1997]]
dates2 = [[1, 1, 1996], [2, 1, 1900], [1, 1, 1900], [31, 12, 1999]]
resultat_esperat = [True, False, False, False]

reduccio = 0
for d1, d2, re in zip(dates1, dates2, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    dia1 = data.Data(d1[0], d1[1], d1[2])
    dia2 = data.Data(d2[0], d2[1], d2[2])
    print("Comment :=>> Data 1: ", dia1)
    print("Comment :=>> Data 2: ", dia2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", re)
    resultat = (dia1 == dia2)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ", resultat)
    if (re == resultat):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> Classe Data: Test del metode __add__")
dates = [[10, 1, 2018], [10, 1, 2018], [10, 1, 2018], [10, 1, 2018],
         [10, 1, 2018], [10, 1, 2018], [20, 12, 2018], [10, 1, 2018]]
n_dies = [0, 1, 21, 31, 59, 90, 31, 365]
resultat_esperat = [[10, 1, 2018], [11, 1, 2018], [31, 1, 2018], [10, 2, 2018],
                    [10, 3, 2018], [10, 4, 2018], [20, 1, 2019], [10, 1, 2019]]

reduccio = 0
for d, nd, re in zip(dates, n_dies, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    dia = data.Data(d[0], d[1], d[2])
    print("Comment :=>> Data: ", dia)
    print("Comment :=>> N. dies: ", nd)
    print("Comment :=>> ---")
    dre = data.Data(re[0], re[1], re[2])
    print("Comment :=>> Resultat esperat: ", dre)
    resultat = dia + nd
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ", resultat)
    if (dre == resultat):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> Classe Llibre: Test del mètode retorna")
data_prestec = [[], [1, 1, 2000], [1, 1, 2000], [1, 1, 2021], [10, 10, 2018],
                [10, 10, 2018], [10, 12, 2018]]
data_retorn = [[], [1, 3, 2000], [2, 3, 2000], [2, 3, 2021], [10, 12, 2018],
               [9, 12, 2018], [8, 2, 2019]]
resultat_esperat = [-1, True, False, True, False, True, True]

reduccio = 0
for dp, dr, re in zip(data_prestec, data_retorn, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    lbre = llibre.Llibre("TITOL", "AUTOR")
    if dp != []:
        dia = data.Data(dp[0], dp[1], dp[2])
        lbre.presta(dia)
        print("Comment :=>> Data prestec: ", dia)
        dia_retorn = data.Data(dr[0], dr[1], dr[2])
        print("Comment :=>> Data retorn: ", dia_retorn)
    else:
        print("Comment :=>> Llibre no prestat")
        dia_retorn = data.Data()
    print("Comment :=>> ---")
    if (re == -1):
        print("Comment :=>> Resultat esperat: ", "AssertionError")
    else:
        print("Comment :=>> Resultat esperat: ", re)
    print("Comment :=>> ---")
    try:
        resultat = lbre.retorna(dia_retorn)
        print("Comment :=>> Resultat obtingut: ", resultat)
    except AssertionError:
        print("Comment :=>> Resultat obtingut: ", "AssertionError")
        resultat = -1
    if (re == resultat):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)


if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
