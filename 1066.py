valores = [float(input()) for i in range(5)]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]
positivos = [valor for valor in valores if valor > 0]
negativos = [valor for valor in valores if valor < 0]

print(f'{len(pares)} valor(es) par(es)')
print(f'{len(impares)} valor(es) impar(es)')
print(f'{len(positivos)} valor(es) positivo(s)')
print(f'{len(negativos)} valor(es) negativo(s)')