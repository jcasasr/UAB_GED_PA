from gestioVendes import GestioVendes

grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")

print ("Comment :=>> Llegint fitxer 'productes.txt' per inicialitzar dades dels productes...........")
print ("Comment :=>> ===============================================================================")
gv = GestioVendes()
gv.llegeixProductes("productes.txt");


print ("Comment :=>> ")
print ("Comment :=>> Test del metode afegeixVendaPresencial")
print ("Comment :=>> ======================================")
reduccio = 0.0
codiProducte = ["CODI_1", "CODI_3", "CODI_6", "CODI_2", "CODI_5", "CODI_7"]
nUnitats = [ 5, 20, 200, 1, 2, 0]
data = [ "01/01/2018", "01/02/2018","01/03/2018","01/04/2018","01/05/2018","01/06/2018" ]
idBotiga = [ "BOTIGA_1", "BOTIGA_2", "BOTIGA_3", "BOTIGA_4", "BOTIGA_5", "BOTIGA_6" ]
importEsperat = [ 50, 570, 10800, 200, 900, -1 ]
i = 1
for codi, n, d, b, ie in zip(codiProducte, nUnitats, data, idBotiga, importEsperat):
    print ("TEST: ", i)
    i += 1
    print ("Comment :=>> Dades de la venda a afegir:")
    print ("Comment :=>> Codi: ", codi)
    print ("Comment :=>> N. unitats: ", n)
    print ("Comment :=>> Data: ", d)
    print ("Comment :=>> Botiga: ", b)
    print ("Comment :=>> ----------")
    print ("Comment :=>> Import venda esperat", ie)
    print ("Comment :=>> ----------")
    io = gv.afegeixVendaPresencial(codi, n, d, b)
    print ("Comment :=>> Import venda obtingut", io)
    if (io == ie):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    print ("Comment :=>> -------------------------------------------------------")
if (reduccio > 6):
    reduccio = 6
grade = grade + (4 - reduccio)
print ("Grade :=>>", grade)


print ("Comment :=>> ")
print ("Comment :=>> Test del metode afegeixVendaOnline")
print ("Comment :=>> ==================================")
reduccio = 0.0
codiProducte = [ "CODI_1", "CODI_3", "CODI_6", "CODI_2", "CODI_5", "CODI_7" ]
nUnitats = [ 5, 20, 200, 1, 2, 0 ]
data = [ "01/01/2018", "01/02/2018","01/03/2018","01/04/2018","01/05/2018","01/06/2018" ]
adreca = [ "ADRECA_1", "ADRECA_2", "ADRECA_3", "ADRECA_4", "ADRECA_5", "ADRECA_6" ]
importEsperat = [ 51, 570.95, 10801.8, 204, 907.2, -1 ]
i = 1
for codi, n, d, a, ie in zip(codiProducte, nUnitats, data, adreca, importEsperat):
    print ("TEST: ", i)
    i += 1
    print ("Comment :=>> Dades de la venda a afegir:")
    print ("Comment :=>> Codi: ", codi)
    print ("Comment :=>> N. unitats: ", n)
    print ("Comment :=>> Data: ", d)
    print ("Comment :=>> Adreça: ", a)
    print ("Comment :=>> ----------")
    print ("Comment :=>> Import venda esperat", ie)
    print ("Comment :=>> ----------")
    io = gv.afegeixVendaOnline(codi, n, d, a)
    print ("Comment :=>> Import venda obtingut", io)
    if (io == ie):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
    print ("Comment :=>> -------------------------------------------------------")
if (reduccio > 6):
    reduccio = 6
grade = grade + (4 - reduccio)
print ("Grade :=>>", grade)

reduccio = 0.0
print ("Comment :=>> ")
print ("Comment :=>> Escrivint resultat al fitxer 'vendes.txt'.....")
print ("Comment :=>> ============================================")
gv.escriuVendes("vendes.txt");
print ("Comment :=>> Comparant fitxer 'vendes.txt' amb fitxer 'vendesResultat.txt'.....")
with open("vendes.txt") as fObtingut:
    with open("vendesResultat.txt") as fEsperat:
        correcte = True
        nLinia = 1;
        liniaObtinguda = fObtingut.readline().rstrip('\n').rstrip(' ')
        liniaEsperada = fEsperat.readline().rstrip('\n').rstrip(' ')
        while correcte and liniaObtinguda != '' and liniaEsperada != '':
            print ("Comment :=>> Linia del ftixer: ", nLinia)
            print ("Comment :=>> Valor esperat: ", liniaEsperada)
            print ("Comment :=>> Valor obtingut: ", liniaObtinguda)
            if liniaObtinguda != liniaEsperada:
                correcte = False
                print ("Comment :=>> ERROR")
            liniaObtinguda = fObtingut.readline().rstrip('\n').rstrip(' ')
            liniaEsperada = fEsperat.readline().rstrip('\n').rstrip(' ')
            nLinia += 1
        if correcte and (liniaObtinguda != '' or  liniaEsperada != ''):
            correcte = False
            print ("Comment :=>> ERROR. FITXERS DE LONGITUD DIFERENT")
        if not correcte:
            reduccio = 5.0;
        else :
            print ("Comment :=>> CORRECTE")
grade = grade + (2 - reduccio)




if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)
print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
