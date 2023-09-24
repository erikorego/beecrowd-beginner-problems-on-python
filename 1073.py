valor = int(input())

numeros_pares = [numero + 1 for numero in range(valor) if (numero + 1) % 2 == 0]

for numero in numeros_pares:
    print(f'{numero}^2 = {numero**2}')