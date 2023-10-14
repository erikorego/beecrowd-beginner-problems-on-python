testes = []
loop = True

while loop:
    teste = input().split(" ")
    for i in range(len(teste)):
        teste[i] = int(teste[i])
    if teste[0] <= 0 or teste[1] <= 0:
        loop = False
    else:
        testes.append(teste)

for teste in testes:
    sequencia = []
    soma = 0
    if teste[0] <= teste[1]:
        for i in range(teste[0], teste[1] + 1):
            sequencia.append(i)
            soma += i
        for numero in sequencia:
            print(numero, end=" ")
        print(f"Sum={soma}")
    else:
        for i in range(teste[0], teste[1] - 1, -1):
            sequencia.append(i)
            soma += i
        sequencia.sort()
        for numero in sequencia:
            print(numero, end=" ")
        print(f"Sum={soma}")