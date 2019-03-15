"""
>>> operaciones = OperacionesAritmeticas()
>>> operaciones.divisionNumeros(23, 2)
11.5
>>> operaciones.divisionNumeros(4, 0)
0
"""
class OperacionesAritmeticas:
    def divisionNumeros(self, operador1, operador2):
        try:
            return operador1 / operador2
        except ZeroDivisionError:
            return 0


if __name__==  '__main__':
    import doctest
    doctest.testmod()