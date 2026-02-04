import racional

grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

print("Comment :=>> Test de la funcio operar (suma)")
print("Comment :=>> =============================")

llistaRacionals = [racional.NombreRacional(1, 2), racional.NombreRacional(4, 12), racional.NombreRacional(
    3, 2), racional.NombreRacional(0, 2), racional.NombreRacional(1, 0), racional.NombreRacional(0, 0)]
operand = racional.NombreRacional(3, 10)
resultatEsperat = [racional.NombreRacional(4, 5), racional.NombreRacional(19, 30), racional.NombreRacional(
    9, 5), racional.NombreRacional(3, 10), racional.NombreRacional(0, 0), racional.NombreRacional(0, 0)]
reduccio = 0
resultatObtingut = racional.operar(llistaRacionals, '+', operand)
for r, re, ro in zip(llistaRacionals, resultatEsperat, resultatObtingut):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Nombre Racional de la llista: ",
          r.numerador, "/", r.denominador)
    print("Comment :=>> Nombre Racional a sumar: ",
          operand.numerador, "/", operand.denominador)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", re.numerador, "/", re.denominador)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ",
          ro.numerador, "/", ro.denominador)
    if (re.numerador == ro.numerador) and (re.denominador == ro.denominador):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.5 - reduccio)
print("Grade :=>>", grade)

print("Comment :=>> Test de la funcio operar (resta)")
print("Comment :=>> ================================")
llistaRacionals = [racional.NombreRacional(1, 2), racional.NombreRacional(4, 12), racional.NombreRacional(
    3, 2), racional.NombreRacional(0, 2), racional.NombreRacional(1, 0), racional.NombreRacional(0, 0)]
operand = racional.NombreRacional(3, 10)
resultatEsperat = [racional.NombreRacional(1, 5), racional.NombreRacional(1, 30), racional.NombreRacional(
    6, 5), racional.NombreRacional(-3, 10), racional.NombreRacional(0, 0), racional.NombreRacional(0, 0)]
reduccio = 0
resultatObtingut = racional.operar(llistaRacionals, '-', operand)
for r, re, ro in zip(llistaRacionals, resultatEsperat, resultatObtingut):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Nombre Racional de la llista: ",
          r.numerador, "/", r.denominador)
    print("Comment :=>> Nombre Racional a restar: ",
          operand.numerador, "/", operand.denominador)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", re.numerador, "/", re.denominador)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ",
          ro.numerador, "/", ro.denominador)
    if ((re.numerador == ro.numerador) and (re.denominador == ro.denominador)) or (
            (re.numerador == -ro.numerador) and (re.denominador == -ro.denominador)):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.5 - reduccio)
print("Grade :=>>", grade)

print("Comment :=>> Test de la funcio operar (multiplica)")
print("Comment :=>> ====================================")
llistaRacionals = [racional.NombreRacional(1, 2), racional.NombreRacional(4, 12), racional.NombreRacional(
    3, 2), racional.NombreRacional(0, 2), racional.NombreRacional(1, 0), racional.NombreRacional(0, 0)]
operand = racional.NombreRacional(3, 10)
resultatEsperat = [racional.NombreRacional(3, 20), racional.NombreRacional(1, 10), racional.NombreRacional(
    9, 20), racional.NombreRacional(0, 1), racional.NombreRacional(0, 0), racional.NombreRacional(0, 0)]
reduccio = 0
resultatObtingut = racional.operar(llistaRacionals, '*', operand)
for r, re, ro in zip(llistaRacionals, resultatEsperat, resultatObtingut):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Nombre Racional de la llista: ",
          r.numerador, "/", r.denominador)
    print("Comment :=>> Nombre Racional a multiplicar: ",
          operand.numerador, "/", operand.denominador)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", re.numerador, "/", re.denominador)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ",
          ro.numerador, "/", ro.denominador)
    if ((re.numerador == ro.numerador) and (re.denominador == ro.denominador)) or (
            (re.numerador == -ro.numerador) and (re.denominador == -ro.denominador)):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.5 - reduccio)
print("Grade :=>>", grade)

print("Comment :=>> Test de la funcio operar (divideix)")
print("Comment :=>> ===================================")
llistaRacionals = [racional.NombreRacional(1, 2), racional.NombreRacional(4, 12), racional.NombreRacional(
    3, 2), racional.NombreRacional(0, 2), racional.NombreRacional(1, 0), racional.NombreRacional(0, 0)]
operand = racional.NombreRacional(3, 10)
resultatEsperat = [racional.NombreRacional(5, 3), racional.NombreRacional(10, 9), racional.NombreRacional(
    5, 1), racional.NombreRacional(0, 1), racional.NombreRacional(0, 0), racional.NombreRacional(0, 0)]
reduccio = 0
resultatObtingut = racional.operar(llistaRacionals, '/', operand)
for r, re, ro in zip(llistaRacionals, resultatEsperat, resultatObtingut):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Nombre Racional de la llista: ",
          r.numerador, "/", r.denominador)
    print("Comment :=>> Nombre Racional a dividir: ",
          operand.numerador, "/", operand.denominador)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", re.numerador, "/", re.denominador)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ",
          ro.numerador, "/", ro.denominador)
    if ((re.numerador == ro.numerador) and (re.denominador == ro.denominador)) or (
            (re.numerador == -ro.numerador) and (re.denominador == -ro.denominador)):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.5 - reduccio)

if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
