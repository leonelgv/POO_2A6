"""
>>> circulo = Circulo(2)
>>> circulo.calcularArea()
>>> circulo.getArea()
12.566370614359172
"""

import math

class Circulo:
    __radio = float(0)
    __perimetro = float(0)
    __area = float(0)

    def __init__(self, radio):
        if(radio < 0):
            self.__radio = 0
        else:
            self.__radio = radio

    def calcularArea(self):
        self.__area = math.pi * (self.__radio * self.__radio)

    def calcularPerimetro(self):
        self.__perimetro = (2 * math.pi) * self.__radio

    def getArea(self):
        return self.__area

    def getPerimetro(self):
        return self.__perimetro

if __name__ ==  '__main__':
    import doctest
    doctest.testmod()