valores = input().split(" ")
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

not_triangulo = (a >= b + c) or (b >= a + c) or (b >= b + a)
retangulo = (a**2 == (b**2 + c**2)) or (b**2 == (a**2 + c**2)) or (c**2 == (b**2 + a**2))
obtusangulo = (a**2 > (b**2 + c**2)) or (b**2 > (a**2 + c**2)) or (c**2 > (b**2 + a**2))
acutangulo = (a**2 < (b**2 + c**2)) or (b**2 < (a**2 + c**2)) or (c**2 < (b**2 + a**2))
equilatero = a == b and b == c and a == c
escaleno  = a != b and b != c and a != c

if not_triangulo:
    print("NAO FORMA TRIANGULO")
else:
    if retangulo:
        print("TRIANGULO RETANGULO")
    elif obtusangulo:
        print("TRIANGULO OBTUSANGULO")
    elif acutangulo:
        print("TRIANGULO ACUTANGULO")

    if equilatero:
        print("TRIANGULO EQUILATERO")
    elif not escaleno:
        print("TRIANGULO ISOSCELES")