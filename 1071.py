inicio = int(input())
fim = int(input())

crescente = inicio < fim
decrescente = fim < inicio

soma = 0

if crescente:
    for valor in range(inicio + 1, fim):
        if valor%2 !=0:
            soma += valor
elif decrescente:
    for valor in range(fim + 1, inicio,):
        if valor%2 !=0:
            soma += valor

print(soma)