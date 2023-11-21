testes = int(input())

for i in range(testes):
    caso = input().split(" ")

    dividendo = float(caso[0])
    divisor = float(caso[1])

    if divisor == 0:
        print("divisao impossivel")
    else:
        divisao = dividendo / divisor
        print(f"{divisao:.1f}")
