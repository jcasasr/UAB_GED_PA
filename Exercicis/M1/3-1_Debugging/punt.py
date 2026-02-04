import math


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, valor):
        self._x = valor

    def get_y(self):
        return self._x

    def set_y(self, valor):
        self._y = valor

    def __sub__(self, p2):
        return math.sqrt((self._x - p2._x)**2 + (self._y - p2._y)**2)

    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")"
