numero_de_testes = int(input())

def media_ponderada (valores):
    for i in range(len(valores)):
        valores[i] = float(valores[i])
    media = ((valores[0] * 2) + (valores[1] * 3) + (valores[2] * 5)) / 10
    return media

testes = []

for i in range(numero_de_testes):
    testes.append(input().split(" "))

for teste in testes:
    print(f"{media_ponderada(teste):.1f}")