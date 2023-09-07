salario = float(input())
reajuste = 0
percentual = 0

if salario <= 400:
    reajuste = salario * 0.15
    percentual = 0.15 * 100
    salario += reajuste
elif salario <= 800:
    reajuste = salario * 0.12
    percentual = 0.12 * 100
    salario += reajuste
elif salario <= 1200:
    reajuste = salario * 0.1
    percentual = 0.1 * 100
    salario += reajuste
elif salario <= 2000:
        reajuste = salario * 0.07
        percentual = 0.07 * 100
        salario += reajuste
elif salario > 2000:
    reajuste = salario * 0.04
    percentual = 0.04 * 100
    salario += reajuste

print(f"Novo salario: {salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual:.0f} %")
