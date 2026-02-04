import sudoku as s
import sys
import numpy as np

def mostra_sudoku(sudoku):
    for fila in sudoku:
        print ("Comment :=>> ", end='')
        for valor in fila:
            print (valor, ' ', end='')
        print(' ')
            
      
grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>> ")

n_partides = 2
resultat_esperat = [
        [False, False, True, False],
		[False, False, False, True, True, False, True, True, True, True, True, True, True]
        ]

sudoku_esperat = np.array([
			[[ 1, 2, 3, 4, 5, 6, 7, 8, 0 ],
			[ 4, 5, 6, 7, 8, 9, 1, 2, 3 ],
			[ 7, 8, 9, 1, 2, 3, 4, 5, 6 ],
			[ 2, 3, 4, 5, 6, 7, 8, 9, 1 ],
			[ 5, 6, 7, 8, 9, 1, 2, 3, 4 ],
			[ 8, 9, 1, 2, 3, 4, 5, 6, 7 ],
			[ 3, 4, 5, 6, 7, 8, 9, 1, 2 ],
			[ 6, 7, 8, 9, 1, 2, 3, 4, 5 ],
			[ 9, 1, 2, 3, 4, 5, 6, 7, 8 ]],
    		[[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
			[ 4, 5, 6, 7, 8, 9, 1, 2, 3 ],
			[ 7, 8, 9, 1, 2, 3, 4, 5, 6 ],
			[ 2, 3, 4, 5, 6, 7, 8, 9, 1 ],
			[ 5, 6, 7, 8, 9, 1, 2, 3, 4 ],
			[ 8, 9, 1, 2, 3, 4, 5, 6, 7 ],
			[ 3, 4, 5, 6, 7, 8, 9, 1, 2 ],
			[ 6, 7, 8, 9, 1, 2, 3, 4, 5 ],
			[ 9, 1, 2, 3, 4, 5, 6, 7, 8 ]]
            ])

valor_test = [4, 6]

for i in range(n_partides):
    reduccio = 0
    nom_test = "test"+str(i+1)+".txt"
    sys.stdin = open(nom_test, 'r')
    print ("Comment :=>> --------------------")
    print ("Comment :=>> Iniciant PARTIDA", i+1)
    print ("Comment :=>> --------------------")
    print ("Comment :=>> Valors del sudoku inicial")
    nom_fitxer = "sudoku"+str(i+1)+".txt"
    sudoku = np.loadtxt(nom_fitxer, dtype='int')
    mostra_sudoku(sudoku)
    print ("Comment :=>> ")
    print ("Comment :=>> Jugant la partida ...")
    print ("Comment :=>> -------")
    sudoku_final, llista_moviments = s.juga_sudoku(nom_fitxer)

    print ("Comment :=>> Valors finals del sudoku esperat")
    mostra_sudoku(sudoku_esperat[i,:,:])
    print ("Comment :=>> -------")
    print ("Comment :=>> Valors finals del sudoku obtingut")
    mostra_sudoku(sudoku_final)
    if (list(sudoku_final.flat) == list(sudoku_esperat[i,:,:].flat)):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 4.0
       
       
    sys.stdin = sys.__stdin__
    with open(nom_test, "r") as fitxer:
        for re, ro in zip(resultat_esperat[i], llista_moviments):
            numero = int(fitxer.readline())
            fila = int(fitxer.readline())
            columna = int(fitxer.readline())
            print ("Comment :=>> -------------------------------")
            print ("Comment :=>> Numero, fila i columna esperats: ", numero, fila, columna)
            print ("Comment :=>> Resultat esperat de fer aquest moviment: ", re)
            print ("Comment :=>> -------")
            print ("Comment :=>> Número, fila i columna i numero obtinguts: ", ro[0], ro[1], ro[2])
            print ("Comment :=>> Resultat obtingut de fer aquest moviment: ", ro[3])
            if (numero == ro[0] and fila == ro[1] and columna == ro[2] and re == ro[3]):
                print ("Comment :=>> CORRECTE")
            else:
                print ("Comment :=>> ERROR")
                reduccio = reduccio + 1.0

    if (reduccio > 8):
        reduccio = 8
    grade = grade + (valor_test[i] - reduccio)
    print ("Grade :=>>", grade)
            
    
    
if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)
print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")




