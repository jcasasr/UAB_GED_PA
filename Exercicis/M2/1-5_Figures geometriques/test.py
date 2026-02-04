import figura
import cercle
import rectangle
import triangle
import operacions_figures
import math
import sys


grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>> ")


print ("Comment :=>> ---------------------------------")
print ("Comment :=>> Iniciant test de la classe Figura")
print ("Comment :=>> ---------------------------------")
reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> Creant objecte de la classe Figura: ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: EXCEPCIO")
print ("Comment :=>> ---")
try:
    fig = figura.Figura()
    print ("Comment :=>> Resultat obtingut: FIGURA CREADA")
    error = True
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = False
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")
grade = grade + (1 - reduccio)
print ("Comment :=>> ")
print ("Grade :=>>", grade)


print ("Comment :=>> ")
print ("Comment :=>> -----------------------------------")
print ("Comment :=>> Iniciant test de la classe Triangle")
print ("Comment :=>> -----------------------------------")
reduccio = 0

vertexs_list = [(0,0, (0,1), (1,1))]
perimetre_esperat_triangle = 3.4142
area_esperada_triangle = 0.5
print ("Comment :=>> ")
print ("Comment :=>> Creant triangle: ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: TRIANGLE CREAT")
print ("Comment :=>> ---")
try:
    trgle = triangle.Triangle()
    print ("Comment :=>> Resultat obtingut: TRIANGLE CREAT")
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Llegint vertexs del triangle: ", vertexs_list)
print ("Comment :=>> ----------------------------------")
sys.stdin = open("test_triangle.txt", 'r')
try:
    trgle.llegeix()
except:
    print ("Comment :=>> EXCEPCIO. ERROR D'EXECUCIO")
    reduccio = reduccio + 1.0
sys.stdin = sys.__stdin__

print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode perimetre...")
print ("Comment :=>> ------------------------------")
print ("Comment :=>> Resultat esperat: ", perimetre_esperat_triangle)
print ("Comment :=>> ---")
try:
    perimetre = trgle.perimetre()
    print ("Comment :=>> Resultat obtingut: ", perimetre)
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
    perimetre = perimetre_esperat_triangle
if not error and (abs(perimetre - perimetre_esperat_triangle) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode area...")
print ("Comment :=>> ------------------------")
print ("Comment :=>> Resultat esperat:", area_esperada_triangle)
print ("Comment :=>> ---")
try:
    area = trgle.area()
    error = False
    print ("Comment :=>> Resultat obtingut: ", area)
except:
    error = True
    area = area_esperada_triangle
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
if not error and (abs(area - area_esperada_triangle) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

grade = grade + (2 - reduccio)
print ("Grade :=>>", grade)


print ("Comment :=>> ")
print ("Comment :=>> ------------------------------------")
print ("Comment :=>> Iniciant test de la classe Rectangle")
print ("Comment :=>> ------------------------------------")
reduccio = 0

top_left = (0,0)
base = 2
alcada = 4
perimetre_esperat_rectangle = 12
area_esperada_rectangle = 8
print ("Comment :=>> ")
print ("Comment :=>> Creant rectangle ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: RECTANGLE CREAT")
print ("Comment :=>> ---")
try:
    rect = rectangle.Rectangle()
    print ("Comment :=>> Resultat obtingut: RECTANGLE CREAT")
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Llegint dades del rectangle. Punt inicial: ", top_left, ", base: ", base, ", alçada: ", alcada )
print ("Comment :=>> ----------------------------------")
sys.stdin = open("test_rectangle.txt", 'r')
try:
    rect.llegeix()
except:
    print ("Comment :=>> EXCEPCIO. ERROR D'EXECUCIO")
    reduccio = reduccio + 1.0
sys.stdin = sys.__stdin__

print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode perimetre...")
print ("Comment :=>> ------------------------------")
print ("Comment :=>> Resultat esperat: ", perimetre_esperat_rectangle)
print ("Comment :=>> ---")
try:
    perimetre = rect.perimetre()
    print ("Comment :=>> Resultat obtingut: ", perimetre)
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
    perimetre = perimetre_esperat_rectangle
if not error and (abs(perimetre - perimetre_esperat_rectangle) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode area...")
print ("Comment :=>> ------------------------")
print ("Comment :=>> Resultat esperat:", area_esperada_rectangle)
print ("Comment :=>> ---")
try:
    area = rect.area()
    error = False
    print ("Comment :=>> Resultat obtingut: ", area)
except:
    error = True
    area = area_esperada_rectangle
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
if not error and (abs(area - area_esperada_rectangle) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

grade = grade + (2 - reduccio)
print ("Grade :=>>", grade)


print ("Comment :=>> ")
print ("Comment :=>> ---------------------------------")
print ("Comment :=>> Iniciant test de la classe Cercle")
print ("Comment :=>> ---------------------------------")
reduccio = 0

centre = (0,0)
radi = 2
perimetre_esperat_cercle = 2 * math.pi * radi
area_esperada_cercle = math.pi * (radi**2)
print ("Comment :=>> ")
print ("Comment :=>> Creant cercle ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: CERCLE CREAT")
print ("Comment :=>> ---")
try:
    cle = cercle.Cercle()
    print ("Comment :=>> Resultat obtingut: CERCLE CREAT")
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Llegint dades del cercle. Punt central: ", centre, ", radi: ", radi)
print ("Comment :=>> ----------------------------------")
sys.stdin = open("test_cercle.txt", 'r')
try:
    cle.llegeix()
except:
    print ("Comment :=>> EXCEPCIO. ERROR D'EXECUCIO")
    reduccio = reduccio + 1.0
sys.stdin = sys.__stdin__

print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode perimetre...")
print ("Comment :=>> ------------------------------")
print ("Comment :=>> Resultat esperat: ", perimetre_esperat_cercle)
print ("Comment :=>> ---")
try:
    perimetre = cle.perimetre()
    print ("Comment :=>> Resultat obtingut: ", perimetre)
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
    perimetre = perimetre_esperat_cercle
if not error and (abs(perimetre - perimetre_esperat_cercle) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode area...")
print ("Comment :=>> ------------------------")
print ("Comment :=>> Resultat esperat:", area_esperada_cercle)
print ("Comment :=>> ---")
try:
    area = cle.area()
    error = False
    print ("Comment :=>> Resultat obtingut: ", area)
except:
    error = True
    area = area_esperada_cercle
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
if not error and (abs(area - area_esperada_cercle) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

grade = grade + (2 - reduccio)
print ("Grade :=>>", grade)


llista_figures = []

print ("Comment :=>> ")
print ("Comment :=>> --------------------------------------------------------------------")
print ("Comment :=>> Iniciant test de les funcions crea_figura, suma_area i max_perimetre")
print ("Comment :=>> --------------------------------------------------------------------")
reduccio = 0

print ("Comment :=>> ")
print ("Comment :=>> Creant i llegint triangle ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: TRIANGLE CREAT")
print ("Comment :=>> Perimetre: ", perimetre_esperat_triangle)
print ("Comment :=>> Area: ", area_esperada_triangle)
print ("Comment :=>> ---")
sys.stdin = open("test_triangle.txt", 'r')
try:
    fig = operacions_figures.crea_figura("T")
    perimetre = fig.perimetre()
    area = fig.area()
    llista_figures.append(fig)
    print ("Comment :=>> Resultat obtingut: TRIANGLE CREAT")
    print ("Comment :=>> Perimetre: ", perimetre)
    print ("Comment :=>> Area: ", area)    
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
sys.stdin = sys.__stdin__
if not error and (abs(perimetre - perimetre_esperat_triangle) < 0.01) and (abs(area - area_esperada_triangle) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Creant i llegint rectangle ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: RECTANGLE CREAT")
print ("Comment :=>> Perimetre: ", perimetre_esperat_rectangle)
print ("Comment :=>> Area: ", area_esperada_rectangle)
print ("Comment :=>> ---")
sys.stdin = open("test_rectangle.txt", 'r')
try:
    fig = operacions_figures.crea_figura("R")
    perimetre = fig.perimetre()
    area = fig.area()
    llista_figures.append(fig)
    print ("Comment :=>> Resultat obtingut: RECTANGLE CREAT")
    print ("Comment :=>> Perimetre: ", perimetre)
    print ("Comment :=>> Area: ", area)    
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
sys.stdin = sys.__stdin__
if not error and (abs(perimetre - perimetre_esperat_rectangle) < 0.01) and (abs(area - area_esperada_rectangle) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Creant i llegint cercle ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: CERCLE CREAT")
print ("Comment :=>> Perimetre: ", perimetre_esperat_cercle)
print ("Comment :=>> Area: ", area_esperada_cercle)
print ("Comment :=>> ---")
sys.stdin = open("test_cercle.txt", 'r')
try:
    fig = operacions_figures.crea_figura("C")
    perimetre = fig.perimetre()
    area = fig.area()
    llista_figures.append(fig)
    print ("Comment :=>> Resultat obtingut: CERCLE CREAT")
    print ("Comment :=>> Perimetre: ", perimetre)
    print ("Comment :=>> Area: ", area)    
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
sys.stdin = sys.__stdin__
if not error and (abs(perimetre - perimetre_esperat_cercle) < 0.01) and (abs(area - area_esperada_cercle) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Calculant suma de l'area de les figures ")
print ("Comment :=>> --------------------------------------- ")
suma_esperada = area_esperada_triangle + area_esperada_rectangle + area_esperada_cercle
print ("Comment :=>> Resultat esperat: ", suma_esperada)
print ("Comment :=>> ---")
try:
    suma = operacions_figures.suma_area(llista_figures)
    print ("Comment :=>> Resultat obtingut: ", suma)
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
if not error and (abs(suma - suma_esperada) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Calculant maxim del perimetre de les figures ")
print ("Comment :=>> -------------------------------------------- ")
maxim_esperat = max(perimetre_esperat_triangle, perimetre_esperat_rectangle, perimetre_esperat_cercle)
print ("Comment :=>> Resultat esperat del perimetre maxim: ", maxim_esperat)
print ("Comment :=>> ---")
try:
    maxim = operacions_figures.max_perimetre(llista_figures)
    print ("Comment :=>> Resultat obtingut del perimetre maxim: ", maxim.perimetre())
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
if not error and (abs(maxim.perimetre() - maxim_esperat) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 1.0
print ("Comment :=>> ----------------------------------")

grade = grade + (3 - reduccio)


if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)
print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
