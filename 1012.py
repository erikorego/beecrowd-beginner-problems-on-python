a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
triangulo = (a * c) / 2
circulo = pi * c**2
trapezio = ((a + b)/2) * c
quadrado = b**2
retangulo = a * b

print(f"TRIANGULO: {triangulo: .3f}\nCIRCULO: {circulo: .3f}\nTRAPEZIO: {trapezio: .3f}\nQUADRADO: {quadrado: .3f}\nRETANGULO: {retangulo: .3f}")