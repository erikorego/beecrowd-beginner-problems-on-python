valor = int(input())
print(valor)

notas_100 = valor // 100
valor %= 100
print(f"{notas_100} nota(s) de R$ 100,00")

notas_50 = valor // 50
valor %= 50
print(f"{notas_50} nota(s) de R$ 50,00")


notas_20 = valor // 20
valor %= 20
print(f"{notas_20} nota(s) de R$ 20,00")


notas_dez = valor // 10
valor %= 10
print(f"{notas_dez} nota(s) de R$ 10,00")


notas_5 = valor // 5
valor %= 5
print(f"{notas_5} nota(s) de R$ 5,00")


notas_dois = valor // 2
valor %= 2
print(f"{notas_dois} nota(s) de R$ 2,00")


notas_um = valor
print(f"{notas_um} nota(s) de R$ 1,00")