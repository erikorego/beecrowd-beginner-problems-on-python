numero_de_entradas = int(input())

valores = []

for entrada in range(numero_de_entradas):
    valor = int(input())
    valores.append(valor)

for valor in valores:
    if valor == 0:
        print("NULL")
    elif valor % 2 == 0:
        if valor > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if valor > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
