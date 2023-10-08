testes = int(input())
resultados = []


for i in range(testes):
    intervalo = input().split(" ")
    inicio = int(intervalo[0])
    fim = int(intervalo[1])
    crescente = inicio <= fim
    soma_impares = 0
    
    if crescente:
        for numero in range(inicio + 1, fim):
            if numero % 2 != 0:
                soma_impares += numero
    else:
        for numero in range(inicio - 1, fim, -1):
            if numero % 2 != 0:
                soma_impares += numero
    resultados.append(soma_impares)

for resultado in resultados:
    print(resultado)
