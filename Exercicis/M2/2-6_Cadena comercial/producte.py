from typing import List, Tuple

            
class Producte:
    _codi: str
    _preu: float

    def __init__(self, codi="", preu=0.0):
        self._codi = codi
        self._preu = preu
        
    def get_codi(self):
        return self._codi

    def set_codi(self, valor):
        self._codi = valor
        
    def get_preu(self):
        return self._preu

    def set_preu(self, valor):
        self._preu = valor

    def llegeix(self):
        self.codi = input("Codi: ")
        self.preu = float(input("Preu: "))

    def mostra(self):
        print ("Codi: ", self.codi)
        print ("Preu: ", self.preu)
        
    def despeses_enviament(self):
        if (self._preu < 100):
            despeses = 1.0
        else:
            despeses = min(5.0, 0.01 * self._preu)
        return despeses


class Llibre(Producte):
    _titol: str
    _autor: str
    _n_pagines: int
    _valoracions: List[Tuple]

    def __init__(self, codi="", preu=0.0, titol="", autor="", n_pagines=0):
        super().__init__(codi, preu)
        self._titol = titol
        self._autor = autor
        self._n_pagines = n_pagines
        self._valoracions = []
    
    def get_titol(self):
        return self._titol
    
    def set_titol(self, valor):
        self._titol = valor

    def get_autor(self):
        return self._autor
    
    def set_autor(self, valor):
        self._autor = valor

    def get_n_pagines(self):
        return self._n_pagines
    
    def set_n_pagines(self, valor):
        self._n_pagines = valor
        
    def llegeix(self):
        super().llegeix()
        self._titol = input("Titol: ")
        self._autor = input("Autor: ")
        self._n_pagines = int(input("N. Pagines: "))

    def afegeix_valoracio(self, puntuacio, missatge):
        self._valoracions.append((puntuacio, missatge))
        
    def despeses_enviament(self):
        despeses = super().despeses_enviament()
        if (self._n_pagines > 500):
            despeses += 1.0
        return despeses

class Electrodomestic(Producte):
    _marca: str
    _model: str
    _volum: float
    _distribuidors: List[str]

    def __init__(self, codi="", preu=0.0, marca="", model="", volum=0.0):
        super().__init__(codi, preu)
        self._marca = marca
        self._model = model
        self._volum = volum
        self._distribuidors = []
          
    def get_marca(self):
        return self._marca
    
    def set_marca(self, valor):
        self._marca = valor

    def get_model(self):
        return self._model

    def set_model(self, valor):
        self._model = valor

    def get_volum(self):
        return self._volum
    
    def set_volum(self, valor):
        self._volum = valor

    def afegeix_distribuidor(self, nom):
        self._distribuidors.append(nom)
        
    def llegeix(self):
        super().llegeix()
        self._marca = input("Marca: ")
        self._model = input("Model: ")
        self._volum = float(input("Volum: "))

    def mostra(self):
        super().mostra()
        print ("Marca: ", self._marca)
        print ("Model: ", self._model)
        print ("Volums: ", self._volum)
        
    def despeses_enviament(self):
        despeses = super().despeses_enviament()
        despeses += int(self._volum / 20)
        return despeses
