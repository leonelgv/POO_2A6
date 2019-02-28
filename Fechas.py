class AnioBisiesto:
    __dia = int(0)
    __mes = int(0)
    __anio = int(0)
    __bisiesto = bool

    def __init__(self, dia, mes, anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    def calcularAnioBisiesto(self):
        return 0