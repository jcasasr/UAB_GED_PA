import sys
from propietat import Casa, Pis

sys.stdin = open("test.txt", 'r')

grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

preu_esperat = [800, 250000, 1000, 225000]
n_test = 0

print("Comment :=>> --------------------")
print("Comment :=>> Creant objecte de tipus CASA amb contracte de LLOGUER: ")
print("Comment :=>> Inicialitzant l'objecte amb les dades de la propietat", n_test + 1, "del fitxer test.txt")
print("\nComment :=>> -----")
print("Comment :=>> Preu esperat: ", preu_esperat[n_test])
c = Casa()
c.llegeix()
preu = c.preu()
print("Comment :=>> -----")
print("Comment :=>> Preu obtingut: ", preu)
if (preu == preu_esperat[n_test]):
    grade += 2.5
    print("Comment :=>> CORRECTE")
else:
    print("Comment :=>> ERROR")
print("Comment :=>> ")
print("Grade :=>>", grade)
n_test += 1

print("Comment :=>> --------------------")
print("Comment :=>> Creant objecte de tipus CASA amb contracte de VENDA: ")
print("Comment :=>> Inicialitzant l'objecte amb les dades de la propietat", n_test + 1, "del fitxer test.txt")
print("Comment :=>> -----")
print("Comment :=>> Preu esperat: ", preu_esperat[n_test])
c = Casa()
c.llegeix()
preu = c.preu()
print("\nComment :=>> -----")
print("Comment :=>> Preu obtingut: ", preu)
if (preu == preu_esperat[n_test]):
    grade += 2.5
    print("Comment :=>> CORRECTE")
else:
    print("Comment :=>> ERROR")
print("Comment :=>> ")
print("Grade :=>>", grade)    
n_test += 1

print("Comment :=>> --------------------")
print("Comment :=>> Creant objecte de tipus PIS amb contracte de LLOGUER: ")
print("Comment :=>> Inicialitzant l'objecte amb les dades de la propietat", n_test + 1, "del fitxer test.txt")
print("Comment :=>> -----")
print("Comment :=>> Preu esperat: ", preu_esperat[n_test])
p = Pis()
p.llegeix()
preu = p.preu()
print("\nComment :=>> -----")
print("Comment :=>> Preu obtingut: ", preu)
if (preu == preu_esperat[n_test]):
    grade += 2.5
    print("Comment :=>> CORRECTE")
else:
    print("Comment :=>> ERROR")
print("Comment :=>> ")
print("Grade :=>>", grade)    
n_test += 1

print("Comment :=>> --------------------")
print("Comment :=>> Creant objecte de tipus PIS amb contracte de VENDA: ")
print("Comment :=>> Inicialitzant l'objecte amb les dades de la propietat", n_test + 1, "del fitxer test.txt")
print("Comment :=>> -----")
print("Comment :=>> Preu esperat: ", preu_esperat[n_test])
p = Pis()
p.llegeix()
preu = p.preu()
print("\nComment :=>> -----")
print("Comment :=>> Preu obtingut: ", preu)
if (preu == preu_esperat[n_test]):
    grade += 2.5
    print("Comment :=>> CORRECTE")
else:
    print("Comment :=>> ERROR")
print("Comment :=>> ")
print("Grade :=>>", grade)    

print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")

sys.stdin = sys.__stdin__