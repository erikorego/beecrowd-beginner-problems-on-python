valor = int(input())

impares = []

while len(impares) < 6:
    if (valor % 2) != 0:
        print(valor)
        impares.append(valor)
    valor += 1

