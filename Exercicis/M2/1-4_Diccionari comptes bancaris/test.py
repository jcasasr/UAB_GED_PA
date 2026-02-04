# -*- coding: utf-8 -*-
import funcions_test as ft

grade = 0
reduccio = 0.0
print("Grade :=>>", grade)


print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

titulars = ['TITULAR_1', 'TITULAR_2', 'TITULAR_3']
saldo_esperat = [700, 1400, 2050]
punts_esperat = 22
bonificacio_esperada = 4.5

print("Comment :=>> ========================================================")
print("Comment :=>> TEST DE LA FUNCIO inicialitza_comptes ")
print("Comment :=>> Crida a la funcio inicialitza_comptes amb el fitxer test_compte.txt")
print("Comment :=>> ")
print("Comment :=>> Comprovant dades dels comptes al diccionari")
comptes = {}
ft.inicialitza_comptes(comptes, 'test_compte.txt')

print("Comment :=>> ---------------------------------")
print("Comment :=>> Titular del compte: ", titulars[0])
print("Comment :=>> Resultat esperat saldo: ", saldo_esperat[0])
print("Comment :=>> ---")
try:
    compte = comptes[titulars[0]]
    print("Comment :=>> Resultat obtingut saldo: ", compte.get_saldo())
    if (saldo_esperat[0] == compte.get_saldo()):
        print("Comment :=>> ")
    else:
        print("Comment :=>> ERROR")
        reduccio += 2.0
except:
    print("Comment :=>> ERRROR. No existeix cap compte amb aquest titular")
    reduccio += 2.0
        
print("Comment :=>> ---------------------------------")
print("Comment :=>> Titular del compte: ", titulars[1])
print("Comment :=>> Resultat esperat saldo: ", saldo_esperat[1])
print("Comment :=>> Resultat esperat punts: ", punts_esperat)
print("Comment :=>> ---")
try:
    compte = comptes[titulars[1]]
    print("Comment :=>> Resultat obtingut saldo: ", compte.get_saldo())
    print("Comment :=>> Resultat obtingut punts: ", compte.get_punts())
    if (saldo_esperat[1] == compte.get_saldo()):
        print("Comment :=>> ")
    else:
        print("Comment :=>> ERROR")
        reduccio += 2.0
except:
    print("Comment :=>> ERRROR. No existeix cap compte jove amb aquest titular")
    reduccio += 2.0


print("Comment :=>> ---------------------------------")
print("Comment :=>> Titular del compte: ", titulars[2])
print("Comment :=>> Resultat esperat saldo: ", saldo_esperat[2])
print("Comment :=>> Resultat esperat bonificacio: ", bonificacio_esperada)
print("Comment :=>> ---")
try:
    compte = comptes[titulars[2]]
    print("Comment :=>> Resultat obtingut saldo: ", compte.get_saldo())
    print("Comment :=>> Resultat obtingut bonificacio: ", compte.get_bonificacio())
    if (saldo_esperat[2] == compte.get_saldo()) and (bonificacio_esperada == compte.get_bonificacio()):
        print("Comment :=>> ")
    else:
        print("Comment :=>> ERROR")
        reduccio += 2.0
except:
    print("Comment :=>> ERRROR. No existeix cap compte nomina amb aquest titular")
    reduccio += 2.0

grade += max(0, (4.0 - reduccio))
print("Grade :=>>", grade)


reduccio = 0.0
print("Comment :=>> ========================================================")
print("Comment :=>> TEST DE LA FUNCIO filtra_moviments")
print("Comment :=>> ")

titulars = ['TITULAR_1', 'TITULAR_2', 'TITULAR_3', 'TITULAR_4']
suma_moviments = [0, 2250, -450, -1]
n_moviments = [0, 2, 2, -1]
for t, suma, n in zip(titulars, suma_moviments, n_moviments):
    print("Comment :=>> ---------------------------------")
    print("Comment :=>> Titular del compte: ", t)
    if n == -1:
        print("Comment :=>> Resultat esperat: ASSERTION")
    else:
        print("Comment :=>> Nº de moviments esperat: ", n)
        print("Comment :=>> Suma esperada de l'import dels moviments: ", suma)
    print("Comment :=>> ---")
    try:
        moviments = ft.filtra_moviments(comptes, t)
        n_moviments_resultat = len(moviments)
        suma_moviments_resultat = sum([m.get_valor() for m in moviments])
        print("Comment :=>> Resultat obtingut nº de moviments: ", n_moviments_resultat)
        print("Comment :=>> Resultat obtingut suma import moviments: ", suma_moviments_resultat)
    except:
        print("Comment :=>> Resultat obtingut: ASSERTION")
        n_moviments_resultat = -1
        suma_moviments_resultat = -1
    if (n_moviments_resultat == n) and (suma_moviments_resultat == suma):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio += 1.0

grade += max(0, (2.0 - reduccio))
print("Grade :=>>", grade)


reduccio = 0.0
print("Comment :=>> ========================================================")
print("Comment :=>> TEST DE LA FUNCIO recupera_moviments")
print("Comment :=>> ")

titulars = ['TITULAR_1', 'TITULAR_2', 'TITULAR_3', 'TITULAR_4']
data_inici = '02/01/2022'
data_fi = '04/01/2022'
n_moviments = [3, 3, 3, -1]
suma_moviments = [-50, -350, -700, -1]
for t, suma, n in zip(titulars, suma_moviments, n_moviments):
    print("Comment :=>> ---------------------------------")
    print("Comment :=>> Titular del compte: ", t)
    print("Comment :=>> Data inici: ", data_inici)
    print("Comment :=>> Data fi: ", data_fi)
    if n == -1:
        print("Comment :=>> Resultat esperat: ASSERTION")
    else:
        print("Comment :=>> Nº de moviments esperat: ", n)
        print("Comment :=>> Suma esperada de l'import dels moviments: ", suma)
    print("Comment :=>> ---")
    try:
        moviments = ft.recupera_moviments(comptes, t, data_inici, data_fi)
        n_moviments_resultat = len(moviments)
        suma_moviments_resultat = sum([m.get_valor() for m in moviments])
        print("Comment :=>> Resultat obtingut nº de moviments: ", n_moviments_resultat)
        print("Comment :=>> Resultat obtingut suma import moviments: ", suma_moviments_resultat)
    except:
        print("Comment :=>> Resultat obtingut: ASSERTION")
        n_moviments_resultat = -1
        suma_moviments_resultat = -1
    if (n_moviments_resultat == n) and (suma_moviments_resultat == suma):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio += 1.0

grade += max(0, (2.0 - reduccio))
print("Grade :=>>", grade)


reduccio = 0.0
print("Comment :=>> ========================================================")
print("Comment :=>> TEST DE LA FUNCIO aplica_bonificacio")
print("Comment :=>> ")

titulars = ['TITULAR_1', 'TITULAR_2', 'TITULAR_3', 'TITULAR_4']
bonificacio = [-1, -1, 0, -1]
saldo = [-1, -1, 2054.5, -1]
for t, b, s in zip(titulars, bonificacio, saldo):
    print("Comment :=>> ---------------------------------")
    print("Comment :=>> Titular del compte: ", t)
    if b == -1:
        print("Comment :=>> Resultat esperat: ASSERTION")
    else:
        print("Comment :=>> Bonificacio final esperada del compte: ", b)
        print("Comment :=>> Saldo final esperat del compte: ", s)
    print("Comment :=>> ---")
    try:
        ft.aplica_bonificacio(comptes, t)
        bonficacio_resultat = comptes[t].get_bonificacio()
        saldo_resultat = comptes[t].get_saldo()
        print("Comment :=>> Resultat obtingut bonificacio final: ", bonficacio_resultat)
        print("Comment :=>> Resultat obtingut saldo final: ", saldo_resultat)
    except:
        print("Comment :=>> Resultat obtingut: ASSERTION")
        bonficacio_resultat = -1
        saldo_resultat = -1
    if (bonficacio_resultat == b) and (saldo_resultat == s):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio += 1.0

grade += max(0, (2.0 - reduccio))
print("Grade :=>>", grade)

print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
