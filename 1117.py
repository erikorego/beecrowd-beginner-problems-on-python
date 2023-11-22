valores = []

while len(valores) < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        valores.append(nota)
    else:
        print("nota invalida")

media = sum(valores)/len(valores)

print(f"media = {media:.2f}")