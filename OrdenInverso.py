import math

class OrdenInverso:
    __entero = int(0)
    __cifra = int(0)

    def __init__(self, entero):
        if(entero > 9999):
            self.__cifra = 0
            self.__entero = 0
        else:
            self.__entero = entero
            self.contarCifras()

    def contarCifras(self):
        num = self.__entero
        contador = 0
        while (int(num / 10) != 0):
            num = int(num / 10)
            contador += 1
        self.__cifra = contador + 1

    def getCifra(self):
        return self.__cifra


oi = OrdenInverso(1000)
print (math.pow(2,3))
math.pow(2,3)
print(oi.getCifra())
