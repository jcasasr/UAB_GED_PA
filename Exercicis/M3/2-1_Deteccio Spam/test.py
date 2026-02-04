import spam
import numpy as np


distancia_esperada = 0.8863
vocabulari = spam.llegeix_vocabulari("vocabulary.txt")
grade = 0
print("Grade :=>>", grade)

bow_resultat = []
print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")
print("Comment :=>> Obtenint representació bow del missatge: 3-1msg1.txt")
bow1 = spam.crea_bow('3-1msg1.txt', vocabulari)
print("Comment :=>> Comparant amb la representació esperada....")
print("Comment :=>> ")
bow_esperat = np.loadtxt("test1.txt")
if (np.all(bow1 == bow_esperat)):
    print("Comment :=>> CORRECTE")
    grade += 3.0
else:
    print("Comment :=>> ERROR")
print("Comment :=>> -----------")
print("Grade :=>>", grade)
print("Comment :=>> ")
print("Comment :=>> -----------------------------------------")

print("Comment :=>> Obtenint representació bow del missatge: 3-1msg2.txt")
bow2 = spam.crea_bow('3-1msg2.txt', vocabulari)
print("Comment :=>> Comparant amb la representació esperada....")
print("Comment :=>> ")
bow_esperat = np.loadtxt("test2.txt")
if (np.all(bow2 == bow_esperat)):
    print("Comment :=>> CORRECTE")
    grade += 3.0
else:
    print("Comment :=>> ERROR")
print("Comment :=>> -----------")
print("Grade :=>>", grade)
print("Comment :=>> ")
print("Comment :=>> -----------------------------------------")

print("Comment :=>> Calculant distància entre la representació dels dos missatges")
distancia = spam.compara_bow(bow1, bow2)
print("Comment :=>> Resultat esperat", distancia_esperada)
print("Comment :=>> -----")
print("Comment :=>> Resultat obtingut", distancia)
if abs(distancia_esperada - distancia) < 0.001:
    print("Comment :=>> CORRECTE")
    grade += 4.0
else:
    print("Comment :=>> ERROR")

print("Comment :=>> -----------")
print("Grade :=>>", grade)
print("Comment :=>> ")
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
