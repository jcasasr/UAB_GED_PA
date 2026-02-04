from funcio_test import test_compte

grade = 0
reduccio = 0.0
print("Grade :=>>", grade)


print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

saldo_esperat = 700
punts_esperat = 12
bonificacio_esperada = 4.5

print("Comment :=>> ========================================================")
print("Comment :=>> TEST DE LA CLASSE CompteCorrent ")
print("Comment :=>> Crida a la funcio test_compte amb el fitxer test_compte.txt")
print("Comment :=>> ")
compte = test_compte('test_compte.txt')

print("Comment :=>> ---------------------------------")
print("Comment :=>> Comprovant dades del compte")
print("Comment :=>> Resultat esperat saldo: ", saldo_esperat)
print("Comment :=>> ---")
print("Comment :=>> Resultat obtingut: ", compte.get_saldo())
if (saldo_esperat == compte.get_saldo()):
    print("Comment :=>> CORRECTE")
    grade += 3.3
else:
    print("Comment :=>> ERROR")
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> TEST DE LA CLASSE CompteJove ")
print("Comment :=>> Crida a la funcio test_compte amb el fitxer test_jove.txt")
print("Comment :=>> ")
compte = test_compte('test_jove.txt')

print("Comment :=>> ---------------------------------")
print("Comment :=>> Comprovant dades del compte")
print("Comment :=>> Resultat esperat saldo: ", saldo_esperat)
print("Comment :=>> Resultat esperat punts: ", punts_esperat)
print("Comment :=>> ---")
print("Comment :=>> Resultat obtingut saldo: ", compte.get_saldo())
print("Comment :=>> Resultat obtingut punts: ", compte.get_punts())
if (saldo_esperat == compte.get_saldo()) and (punts_esperat == compte.get_punts()):
    print("Comment :=>> CORRECTE")
    grade += 3.3
else:
    print("Comment :=>> ERROR")
print("Grade :=>>", grade)


print("Comment :=>> ========================================================")
print("Comment :=>> TEST DE LA CLASSE CompteNomina ")
print("Comment :=>> Crida a la funcio test_compte amb el fitxer test_nomina.txt")
print("Comment :=>> ")
compte = test_compte('test_nomina.txt')

print("Comment :=>> ---------------------------------")
print("Comment :=>> Comprovant dades del compte")
print("Comment :=>> Resultat esperat saldo: ", saldo_esperat)
print("Comment :=>> Resultat esperat bonificacio: ", bonificacio_esperada)
print("Comment :=>> ---")
print("Comment :=>> Resultat obtingut saldo: ", compte.get_saldo())
print("Comment :=>> Resultat obtingut bonificacio: ", compte.get_bonificacio())
if (saldo_esperat == compte.get_saldo()) and (bonificacio_esperada == compte.get_bonificacio()):
    print("Comment :=>> CORRECTE")
    grade += 3.4
else:
    print("Comment :=>> ERROR")
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
