"""Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: 
um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e
 menor que a soma dos outros dois lados."""

valores = input().split(" ")
for i in range(len(valores)):
    valores[i] = float(valores[i])

a = valores[0]
b = valores[1]
c = valores[2]

#Condições:
lado_a = a > abs(c-b) and a < c + b
lado_b = a > abs(c-a) and b < c + a
lado_c = a > abs(a-b) and c < a + b
triangulo = lado_a and lado_b and lado_c

if triangulo:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")