class ContadorDecimales:
    __numero = float(0)
    __totalCifras = int(0)

    def __init__(self, numero):
        self.__numero = numero

    def contadorCifrasDecimales(self):
        contador = 0
        num = self.__numero

        while True:
            num = num * 10
            if(num % 10 == 0):
                break
            contador