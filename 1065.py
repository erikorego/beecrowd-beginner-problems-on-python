valores = [float(input()) for i in range(5)]
pares = [valor for valor in valores if valor % 2 == 0]
print(f'{len(pares)} valores pares')