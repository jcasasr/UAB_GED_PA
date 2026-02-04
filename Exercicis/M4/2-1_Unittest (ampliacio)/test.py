import unittest
from unit_test import TestVector


grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")
print("Comment :=>> Executant tots els tests de la classe TestVector......")
print("Comment :=>> ")

suite = unittest.TestSuite()
load_from = unittest.defaultTestLoader.loadTestsFromTestCase
suite.addTests(load_from(TestVector))

runner = unittest.TextTestRunner()
result = runner.run(suite)

print("Comment :=>> --------------------------------------------")
print("Comment :=>> Comprovant resultat del test")
print("Comment :=>> ")
print("Comment :=>> --------------------------------------------")
print("Comment :=>> Nº mínim de tests executats esperat: 15")
print("Comment :=>> ---")
print("comment: =>> Nº de tests executats: ", result.testsRun)
if result.testsRun >= 15:
    print("Comment :=>> CORRECTE")
    grade += 2
else:
    print("Comment :=>> ERROR")
print("Grade :=>>", grade)
print("Comment :=>> ")
print("Comment :=>> --------------------------------------------")

print("Comment :=>> Nº mínim esperat de tests que no donen el resultat esperat: 5")
print("Comment :=>> ---")
print("comment: =>> Nº de tests que no donen el resultat esperat: ", len(result.failures))
if len(result.failures) >= 5:
    print("Comment :=>> CORRECTE")
    grade += 6
else:
    print("Comment :=>> ERROR")
    grade += len(result.failures)
print("Grade :=>>", grade)
print("Comment :=>> ")
print("Comment :=>> ---")
print("Comment :=>> Informació dels tests:")
for f in result.failures:
    print("Comment :=>> ", f)
print("Comment :=>> --------------------------------------------")

print("Comment :=>> Nº mínim esperat de tests que generen una excepció no controlada: 1")
print("Comment :=>> ---")
print("comment: =>> Nº de tests que generen una excepció no controlada: ", len(result.errors))
if len(result.errors) >= 1:
    print("Comment :=>> CORRECTE")
    grade += 2
else:
    print("Comment :=>> ERROR")
print("Grade :=>>", grade)
print("Comment :=>> ")
print("Comment :=>> ---")
print("Comment :=>> Informació dels tests:")
for f in result.errors:
    print("Comment :=>> ", f)
print("Comment :=>> --------------------------------------------")

print("Comment :=>> Nº màxim esperat de tests que generen algun error: 10")
print("Comment :=>> ---")
print("comment: =>> Nº de tests que generen algun error: ",
      len(result.failures) + len(result.errors))
if len(result.failures) + len(result.errors) <= 10:
    print("Comment :=>> CORRECTE")
else:
    grade -= 5
    print("Comment :=>> ERROR")
    if grade < 0:
        grade = 0
print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")