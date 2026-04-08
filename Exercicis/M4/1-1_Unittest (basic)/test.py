import unittest
from unit_test import TestVector


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
print("Comment :=>> --------------------------------------------")
print("comment: =>> Nº de tests executats: ", result.testsRun)
print("Comment :=>> --------------------------------------------")
print("comment: =>> Nº de tests que no donen el resultat esperat: ", len(result.failures))
print("Comment :=>> Informació dels tests:")
for f in result.failures:
    print("Comment :=>> ", f)
print("Comment :=>> --------------------------------------------")
print("comment: =>> Nº de tests que generen una excepció no controlada: ", len(result.errors))
print("Comment :=>> Informació dels tests:")
for f in result.errors:
    print("Comment :=>> ", f)
print("Comment :=>> --------------------------------------------")
print("comment: =>> Nº de tests que generen algun error: ", len(result.failures) + len(result.errors))
print("Comment :=>> --------------------------------------------")
