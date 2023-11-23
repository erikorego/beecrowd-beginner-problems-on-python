def media():
    valores = []
    while len(valores) < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            valores.append(nota)
        else:
            print("nota invalida")
    media = sum(valores) / len(valores)
    return media

print(f"media = {media():.2f}")
print("novo calculo (1-sim 2-nao)")
novo_calculo = int(input())

while novo_calculo != 2:
    if novo_calculo == 1:
        print(f"media = {media():.2f}")
        print("novo calculo (1-sim 2-nao)")
        novo_calculo = int(input())
    elif novo_calculo != 1 and novo_calculo != 2:
        print("novo calculo (1-sim 2-nao)")
        novo_calculo = int(input())