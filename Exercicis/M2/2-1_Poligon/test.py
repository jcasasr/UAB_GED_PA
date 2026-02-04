import math
import poligon

grade = 0
print("Grade :=>>", grade)

print("Comment :=>> Iniciant test")
print("Comment :=>> =============")
print("Comment :=>> ")

llista_punts = [(1, 0), (0, 1), (1, 2), (1, 1), (2, 0), (1, 0)]
perimetre_esperat = 2 + 3 * (math.sqrt(2))
sup_esq_esperat = (0, 0)
inf_dreta_esperat = (2, 2)
resultat_funcio_esperat = [perimetre_esperat, sup_esq_esperat, inf_dreta_esperat]

print("Comment :=>> ========================================================")
print("Comment :=>> Creant poligon amb vertexs: ", llista_punts)
print("Comment :=>> ")
pol = poligon.Poligon()
for p in llista_punts:
    pol.afegeix_vertex(poligon.Punt(p[0], p[1]))
print("Comment :=>> ---------------------------------")
print("Comment :=>> Test del mètode calcula_perimetre")
print("Comment :=>> Resultat esperat: ", perimetre_esperat)
resultat = pol.calcula_perimetre()
print("Comment :=>> ---")
print("Comment :=>> Resultat obtingut: ", resultat)
if (perimetre_esperat == resultat):
    print("Comment :=>> CORRECTE")
    grade = grade + 2.0
else:
    print("Comment :=>> ERROR")
print("Grade :=>>", grade)

print("Comment :=>> ---------------------------------")
print("Comment :=>> Test de la propietat superior_esquerra")
print("Comment :=>> Resultat esperat: ", sup_esq_esperat)
resultat = pol.get_superior_esquerra()
print("Comment :=>> ---")
print("Comment :=>> Resultat obtingut: ", (resultat.get_x(), resultat.get_y()))
if (sup_esq_esperat == (resultat.get_x(), resultat.get_y())):
    print("Comment :=>> CORRECTE")
    grade = grade + 2.0
else:
    print("Comment :=>> ERROR")
print("Grade :=>>", grade)

print("Comment :=>> ---------------------------------")
print("Comment :=>> Test de la propietat inferior_dreta")
print("Comment :=>> Resultat esperat: ", inf_dreta_esperat)
resultat = pol.get_inferior_dreta()
print("Comment :=>> ---")
print("Comment :=>> Resultat obtingut: ", (resultat.get_x(), resultat.get_y()))
if (inf_dreta_esperat == (resultat.get_x(), resultat.get_y())):
    print("Comment :=>> CORRECTE")
    grade = grade + 2.0
else:
    print("Comment :=>> ERROR")
print("Grade :=>>", grade)

print("Comment :=>> ---------------------------------")
print("Comment :=>> Test de la funcio test_poligon amb punts: ", llista_punts)
print("Comment :=>> Resultat esperat: ", resultat_funcio_esperat)
resultat = poligon.test_poligon(llista_punts)
print("Comment :=>> ---")
print("Comment :=>> Resultat obtingut: ", resultat)
if (resultat_funcio_esperat == resultat):
    print("Comment :=>> CORRECTE")
    grade = grade + 4.0
else:
    print("Comment :=>> ERROR")
print("Grade :=>>", grade)

print("Grade :=>>", grade)
print("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print("Comment :=>> Final del test sense errors")
print("Grade :=>> ", grade)
