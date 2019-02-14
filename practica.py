from Recibo import Recibo
from Circulo import Circulo

recibo = Recibo(12.16, 1200, 800)
recibo.calcularCosto()
print ('El pago del recibo es de: ', recibo.getTotalAPagar())

recibo2 = Recibo(9, 1000, 300)
recibo2.calcularCosto()
print ('El pago del segundo recibo es de: ', recibo2.getTotalAPagar())

micirculo = Circulo(23)

print ('El área del circulo es: ', micirculo.getArea())
print ('El perimetro del circulo es: ', micirculo.getPerimetro())

otroCirculo = Circulo(15)


print ('El área del circulo es: ', otroCirculo.getArea())
print ('El perimetro del circulo es: ', otroCirculo.getPerimetro())
