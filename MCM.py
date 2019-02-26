class MCM:
    __num1 = int(0)
    __num2 = int(0)
    __num3 = int(0)
    __mcm = int(0)

    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
        self.calcularMCM()

    def getMCM(self):
        return self.__mcm

    def calcularMCM(self):
        num1 = self.__num1
        num2 = self.__num2
        num3 = self.__num3
        self.__mcm = 1
        divisor = 2
        while True:
            if (num1 % divisor == 0 or num2 % divisor == 0 or num3 % divisor == 0):
                self.__mcm = self.__mcm * divisor
            if (num1 % divisor == 0):
                num1 = num1 / divisor
            if (num2 % divisor == 0):
                num2 = num2 / divisor
            if (num3 % divisor == 0):
                num3 = num3 / divisor
            if (num1 % divisor != 0 and num2 % divisor != 0 and num3 % divisor != 0):
                divisor = divisor + 1
            if(num1 == 1 and num2 == 1 and num3 == 1):
                break

mcm = MCM(8, 24, 50)
print (mcm.getMCM())