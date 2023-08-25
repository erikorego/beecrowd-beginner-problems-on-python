valor_escolhido = float(input())
NOTAS = [100, 50, 20, 10, 5, 2]
MOEDAS = [100, 50, 25, 10, 5, 1]
print("NOTAS:")
for valor in NOTAS:
    numero_notas = valor_escolhido // valor
    print(f"{numero_notas:.0f} nota(s) de R$ {valor:.2f}")
    valor_escolhido %= valor

valor_escolhido *= 100
print("MOEDAS:")
for valor in MOEDAS:
    numero_moedas = valor_escolhido // valor
    print(f"{numero_moedas:.0f} moeda(s) de R$ {(valor/100):.2f}")
    valor_escolhido %= valor