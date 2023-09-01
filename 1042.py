valores = input().split(" ")

for i in range(len(valores)):
    valores[i] = int(valores[i])

ascedent_order = sorted(valores)

for valor in ascedent_order:
    print(valor)

print()

for valor in valores:
    print(valor)