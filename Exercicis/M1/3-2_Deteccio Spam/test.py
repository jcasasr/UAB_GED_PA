import spam


resultat_esperat = []
with open("test.txt", "r") as fitxer:
    for i in range(10):
        nom = fitxer.readline().rstrip()
        label = eval(fitxer.readline().rstrip())
        distancies = eval(fitxer.readline().rstrip())
        resultat_esperat.append((nom, label, distancies))

grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")
print("Comment :=>> Executant classificació dels missatges......")
print("Comment :=>> ")
resultat = spam.deteccio_spam('train/', 'test/', 'vocabulary.txt', 5)
resultat.sort(key=lambda document: document[0])
for i, re in enumerate(resultat_esperat):
    reduccio = 0
    print("Comment :=>> -----------------------------------------")
    print("Comment :=>> Missatge de test: ", resultat_esperat[i][0])
    print("Comment :=>> -----------------------------------------")
    print("Comment :=>> Resultat esperat de la classificació: ",
          resultat_esperat[i][1])
    print("Comment :=>> ---")
    print("Comment :=>> Resultat obtingut de la classificació: ",
          resultat[i][1])
    if (resultat_esperat[i][1] == resultat[i][1]):
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    print("Comment :=>> ------------------------------------------")
    print("Comment :=>> ")
    print("Comment :=>> Comparant valors de les distàncies...")
    print("Comment :=>> ")
    correcte = True
    for de, d in zip(resultat_esperat[i][2], resultat[i][2]):
        correcte = correcte and (abs(d - de) < 0.01)
    if correcte:
        print("Comment :=>> CORRECTE")
    else:
        print("Comment :=>> ERROR")
        print("Comment :=>> Distàncies esperades: ", resultat_esperat[i][2])
        print("Comment :=>> Distàncies obtingudes: ", resultat[i][2])
        reduccio = reduccio + 1.0
    print("Comment :=>> ------------------------------------------")

    if (reduccio > 2):
        reduccio = 2
    grade = grade + (1 - reduccio)
    print("Grade :=>>", grade)

if (grade < 0):
    grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
