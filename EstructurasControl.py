"""
>>> EC = EstructurasControl()
>>> EC.estructuraIf(80)
True
>>> EC.estructuraIf(60)
False
>>> EC.estructuraIf(110)
False
>>> EC.obtenerOctalNumero(3739)
7233
"""

import math

class EstructurasControl:

    # Método de prueba de la estructura de control condicional IF
    # recibe de entrada el valor de una nota y muestra de salida
    # True si la nota tiene un valor de 70 a 100 y False si es menor
    # a 70 y mayor a 100

    """
    Método de prueba de la estructura de control condicional IF
    recibe de entrada el valor de una nota y muestra de salida
    True si la nota tiene un valor de 70 a 100 y False si es menor
    a 70 y mayor a 100
    """

    def estructuraIf(self, nota):
        # Determina si la nota esta en el rango de 70 a 100
        if(nota>70 and nota<100):
            return True
        else:
            return False

    def tablaMultiplicar(self, numero):
        for a in range(1, 101, 2):
            print(numero, "x", a, "=", (numero * a))

    def obtenerOctalNumero(self, numero):
        div1 = numero
        acumulador = 1
        resultado = 0
        while True:
            # Se guarda el residuo de división
            res = div1 % 8
            div1 = int(div1 / 8)
            resultado = res * acumulador + resultado
            acumulador = acumulador * 10
            if (div1 == 0):
                break
        return resultado

    def switch_demo(self, argument):
        switcher = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        print (switcher.get(argument, "Invalid month"))

EC = EstructurasControl()
EC.switch_demo(4)

if __name__==  '__main__':
    import doctest
    doctest.testmod()