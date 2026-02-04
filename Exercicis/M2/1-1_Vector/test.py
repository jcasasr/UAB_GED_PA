import vector


grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

print("Comment :=>> ========================================================")
print("Comment :=>> Test del metode __str__")
vector_inicial = [[1], [1, 2], [1, 2, 3]]
resultat_esperat = ["[1]", "[1,2]", "[1,2,3]"]
reduccio = 0
for vi, s in zip(vector_inicial, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Vector construit a partir de la llista: ", vi)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", s)
    v = vector.Vector(vi)
    resultat = v.__str__()
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut: ", resultat)
    if (s == resultat):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)

print("Comment :=>> ========================================================")
print("Comment :=>> Test del metode __add__")
vector_inicial = [1, 2, 3]
vector_suma = [[1, 2], [0, 0, 0], [1, 2, 3, 4], [1, 1, 1]]
resultat_esperat = [[], [1, 2, 3], [], [2, 3, 4]]
reduccio = 0
for vs, re in zip(vector_suma, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Vector inicial: ", vector_inicial)
    print("Comment :=>> Vector a sumar: ", vs)
    print("Comment :=>> ---")
    if (re == []):
        print("Comment :=>> Resultat esperat: EXCEPCIO")
    else:
        print("Comment :=>> Resultat esperat: ", re)
    print("Comment :=>> ---")
    try:
        v = vector.Vector(vector_inicial)
        resultat = v + vector.Vector(vs)
        print("Comment :=>> Resultat obtingut: ", resultat.__str__())
        sro = resultat.__str__()
    except ValueError:
        print("Comment :=>> Resultat obtingut: EXCEPCIO")
        sro = ""
    if re == []:
        sre = ""
    else:
        vre = vector.Vector(re)
        sre = vre.__str__()
    if (sre == sro):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)

print("Comment :=>> ========================================================")
print("Comment :=>> Test del metode __sub__")
vector_inicial = [1, 2, 3]
vector_resta = [[1, 2], [0, 0, 1], [1, 2, 3, 4], [1, 5, 7]]
resultat_esperat = [-1, 3, -1, 5]
reduccio = 0
for vr, re in zip(vector_resta, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Vector inicial: ", vector_inicial)
    print("Comment :=>> Vector a restar: ", vr)
    print("Comment :=>> ---")
    if (re == -1):
        print("Comment :=>> Resultat esperat: EXCEPCIO")
    else:
        print("Comment :=>> Resultat esperat: ", re)
    print("Comment :=>> ---")
    try:
        v = vector.Vector(vector_inicial)
        resultat = v - vector.Vector(vr)
        print("Comment :=>> Resultat obtingut: ", resultat)
        ro = resultat
    except ValueError:
        print("Comment :=>> Resultat obtingut: EXCEPCIO")
        ro = -1
    if (re == ro):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)

print("Comment :=>> ========================================================")
print("Comment :=>> Test del metode __mul__")
vector_inicial = [1, 2, 3]
vector_mult = [[1, 2], [0, 0, 1], [1, 2, 3, 4], [1, 5, 7]]
resultat_esperat = [-1, 3, -1, 32]
reduccio = 0
for vm, re in zip(vector_mult, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Vector inicial: ", vector_inicial)
    print("Comment :=>> Vector a multiplicar: ", vm)
    print("Comment :=>> ---")
    if (re == -1):
        print("Comment :=>> Resultat esperat: EXCEPCIO")
    else:
        print("Comment :=>> Resultat esperat: ", re)
    print("Comment :=>> ---")
    try:
        v = vector.Vector(vector_inicial)
        resultat = v * vector.Vector(vm)
        print("Comment :=>> Resultat obtingut: ", resultat)
        ro = resultat
    except ValueError:
        print("Comment :=>> Resultat obtingut: EXCEPCIO")
        ro = -1
    if (re == ro):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2 - reduccio)
print("Grade :=>>", grade)

print("Comment :=>> ========================================================")
print("Comment :=>> Test de la funcio opera_vectors")
vector_1 = [1, 2, 3]
vector_2 = [[1, 2], [0, 0, 1], [1, 2, 3, 4], [1, 5, 7], [1, 1, 1]]
operacio = ['+', '-', '*', '+', '*']
resultat_esperat = [None, 3, None, [2, 7, 10], 6]
reduccio = 0
for v2, op, re in zip(vector_2, operacio, resultat_esperat):
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> Vector 1: ", vector_1)
    print("Comment :=>> Vector 2: ", v2)
    print("Comment :=>> Operacio: ", op)
    print("Comment :=>> ---")
    print("Comment :=>> Resultat esperat: ", re)
    print("Comment :=>> ---")
    resultat = vector.opera_vectors(vector_1, v2, op)
    if op == '+' and resultat != None and re != None:
        print("Comment :=>> Resultat obtingut: ", resultat.__str__())
        vre = vector.Vector(re)
        sre = vre.__str__()
        if (sre == resultat.__str__()):
            print("Comment :=>> CORRECTE")
        else:
            print("Comment :=>> ERROR")
            reduccio = reduccio + 2.0
    else:
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

if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
