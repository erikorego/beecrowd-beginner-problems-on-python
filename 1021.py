valor = float(input())

print("NOTAS:")

notas_100 = valor // 100
valor %= 100
print(f"{notas_100:.0f} nota(s) de R$ 100.00")

notas_50 = valor // 50
valor %= 50
print(f"{notas_50:.0f} nota(s) de R$ 50.00")


notas_20 = valor // 20
valor %= 20
print(f"{notas_20:.0f} nota(s) de R$ 20.00")


notas_dez = valor // 10
valor %= 10
print(f"{notas_dez:.0f} nota(s) de R$ 10.00")


notas_5 = valor // 5
valor %= 5
print(f"{notas_5:.0f} nota(s) de R$ 5.00")


notas_dois = valor // 2
valor %= 2
print(f"{notas_dois:.0f} nota(s) de R$ 2.00")

print("MOEDAS:")
moeda_um_real = valor // 1
valor %= 1
print(f"{moeda_um_real:.0f} moeda(s) de R$ 1.00")

valor *= 100

moeda_50 = valor // 50
valor %= 50
print(f"{moeda_50:.0f} moeda(s) de R$ 0.50")

moeda_25 = valor // 25
valor %= 25
print(f"{moeda_25:.0f} moeda(s) de R$ 0.25")

moeda_dez = valor // 10
valor %= 10
print(f"{moeda_dez:.0f} moeda(s) de R$ 0.10")

moeda_cinco = valor // 5
valor %= 5
print(f"{moeda_cinco:.0f} moeda(s) de R$ 0.05")

moeda_um = valor
print(f"{moeda_um:.0f} moeda(s) de R$ 0.01")
