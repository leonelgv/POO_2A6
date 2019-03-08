from Recibo import Recibo
from Circulo import Circulo
from EstructurasControl import EstructurasControl

recibo = Recibo(12.16, 1200, 800)
recibo.calcularCosto()
print ('El pago del recibo es de: ', recibo.getTotalAPagar())

recibo2 = Recibo(9, 1000, 300)
recibo2.calcularCosto()
print ('El pago del segundo recibo es de: ', recibo2.getTotalAPagar())

micirculo = Circulo(2)

print ('El área del circulo es: ', micirculo.getArea())
print ('El perimetro del circulo es: ', micirculo.getPerimetro())

otroCirculo = Circulo(-15)


print ('El área del circulo es: ', otroCirculo.getArea())
print ('El perimetro del circulo es: ', otroCirculo.getPerimetro())


hora = 0
minuto = 59
segundo = 59

segundo = segundo + 1


print (hora, minuto, segundo)

EC = EstructurasControl()

a = EC.obtenerOctalNumero(7686786)
b = EC.obtenerOctalNumero(789798)
