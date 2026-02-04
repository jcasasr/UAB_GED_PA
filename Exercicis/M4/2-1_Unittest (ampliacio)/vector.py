import math


class Vector:
    def __init__(self, valors):
        self.valors = valors

    def __str__(self):
        sortida = "["
        if len(self.valors) > 0:
            sortida = sortida + str(self.valors[0])
            for v in self.valors[1:]:
                sortida = sortida + "," + str(v)
        sortida = sortida + "]"
        return sortida

    def __add__(self, v):
        assert len(self.valors) == len(
            self.valors), "Longitud de vectors diferent"
        suma = [v1 + v2 for v1, v2 in zip(self.valors, v.valors)]
        return Vector(suma)

    def __sub__(self, v):
        assert len(self.valors) == len(
            v.valors), "Longitud de vectors diferent"
        distancia = [(v1 - v2) for v1, v2 in zip(self.valors, v.valors)]
        return math.sqrt(sum(distancia))

    def __mul__(self, v):
        assert len(self.valors) == len(
            v.valors), "Longitud de vectors incorrecta"
        multiplicacio = sum([v1 + v2 for v1, v2 in zip(self.valors, v.valors)])
        return multiplicacio