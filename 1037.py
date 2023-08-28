valor = float(input())

intervalo1 = valor >= 0 and valor <= 25
intervalo2 = valor > 25 and valor <= 50
intervalo3 = valor > 50 and valor <= 75
intervalo4 = valor > 75 and valor <= 100

if intervalo1:
    print("Intervalo [0,25]")
elif intervalo2:
    print("Intervalo (25,50]")
elif intervalo3:
    print("Intervalo (50,75]")
elif intervalo4:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")