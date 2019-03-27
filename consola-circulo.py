from Circulo import *

radio = float(input("Escribe el radio: "))
circulo = Circulo(radio)
print ('El área del circulo es: ', circulo.getArea())
print ('El perimetro del circulo es: ', circulo.getPerimetro())

radio = float(input("Escribe el radio: "))
circulo2 = Circulo(radio)
print ('El área del circulo es: ', circulo2.getArea())
print ('El perimetro del circulo es: ', circulo2.getPerimetro())

print ("La suma de las áreas de los circulos es: ", (circulo.getArea() + circulo2.getArea()))