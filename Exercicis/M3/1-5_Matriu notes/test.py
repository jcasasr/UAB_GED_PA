import exercici
import numpy as np


def mostraMatriu(matriu):
    for fila in matriu:
        print ("Comment :=>> ", fila)
        
grade = 0
print ("Grade :=>>", grade)


print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>> ")


print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio mitjanaLliuraments" )
notes = np.array([[6, 8, 10], [-1, 8, 10], [-1, -1, 10], [0, 0, 0]])
print ("Comment :=>> ")
print ("Comment :=>> Matriu de notes: ")
mostraMatriu(notes)
estudiant = range(4)
resultatEsperat = [8, 0, 0, 0]
reduccio = 0
for notaEsperada, e in zip(resultatEsperat, estudiant):
    print ("Comment :=>> ------------------------------------------")
    print ("Comment :=>> Estudiant numero: ", e)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", notaEsperada)
    nota = exercici.mitjanaLliuraments(notes, e)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut: ", nota)
    if (nota == notaEsperada):    
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.5 - reduccio)
print ("Grade :=>>", grade)



print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio nAprovats" )
notes = np.array([[6, 8, 10], [4, 5, 6], [4, 4, 4], [-1, 8, 10], [-1, -1, 10], [0, 0, 0]])
print ("Comment :=>> ")
print ("Comment :=>> Matriu de notes: ")
mostraMatriu(notes)
resultatEsperat = 2
reduccio = 0
print ("Comment :=>> ---")
print ("Comment :=>> Resultat esperat: ", resultatEsperat)
n = exercici.nAprovats(notes)
print ("Comment :=>> ---")
print ("Comment :=>> Resultat obtingut: ", n)
if (n == resultatEsperat):    
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.5
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.5 - reduccio)
print ("Grade :=>>", grade)



print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio resultatExercici" )
notes = np.array([[6, 8, 10], [-1, 7, 10], [-1, -1, 10], [0, 0, 0]])
print ("Comment :=>> ")
print ("Comment :=>> Matriu de notes: ")
mostraMatriu(notes)
exercicis = range(3)
resultatEsperat = [(2, 0, 6, 3), (3, 0, 8, 5), (4, 0, 10, 7.5)]
reduccio = 0
for notesEsperades, ex in zip(resultatEsperat, exercicis):
    print ("Comment :=>> ------------------------------------------")
    print ("Comment :=>> Exercici numero: ", ex)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", notesEsperades)
    resultat = exercici.resultatExercici(notes, ex)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut: ", resultat)
    if (resultat == notesEsperades):    
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 2.0
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.5 - reduccio)
print ("Grade :=>>", grade)



print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio abandonamentsSetmanals" )
notes = np.array([[-1, -1, -1], [4, 5, -1], [4, 4, -1], [-1, 8, 10], [-1, -1, 10], [-1, -1, -1]])
print ("Comment :=>> ")
print ("Comment :=>> Matriu de notes: ")
mostraMatriu(notes)
resultatEsperat = [2, 0, 2]
reduccio = 0
print ("Comment :=>> ---")
print ("Comment :=>> Resultat esperat: ", resultatEsperat)
a = exercici.abandonamentsSetmanals(notes)
print ("Comment :=>> ---")
print ("Comment :=>> Resultat obtingut: ", a)
if (a == resultatEsperat):    
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.5
if (reduccio > 4):
    reduccio = 4
grade = grade + (2.5 - reduccio)
print ("Grade :=>>", grade)




if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)
print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
