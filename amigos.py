"""
>>> amigos = Amigos(-2, 3)
>>> amigos.getAmigos()
False
"""
class Amigos:
    __numero1 = int(0)
    __numero2 = int(0)
    __amigos = bool

    def __init__(self, numero1, numero2):
        if (numero1 > 0 and numero2 > 0):
            self.__numero1 = numero1
            self.__numero2 = numero2
            self.sonAmigos()
        else:
            self.__numero1 = 0
            self.__numero2 = 0
            self.__amigos = False

    def sumarDivisores(self, numero):
        suma = 0
        for a in range(1, numero, 1):
            if (numero % a) == 0:
                suma += a
        return suma

    def sonAmigos(self):
        if (self.sumarDivisores(self.__numero1) == self.sumarDivisores(self.__numero2)):
            self.__amigos = True
        else:
            self.__amigos = False

    def getAmigos(self):
        return self.__amigos

if __name__==  '__main__':
    import doctest
    doctest.testmod()

