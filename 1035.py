valores = input().split(" ")

for i in range(len(valores)):
    valores[i] = int(valores[i])

c1 = valores[1] > valores[2]
c2 = valores[3] > valores[0]
c3 = (valores[2] + valores[3]) > (valores[0] + valores[1])
c4 = valores[2] > 0 and valores[3] > 0
c5 = valores[0] % 2 == 0

if c1 and c2 and c3 and c4 and c5:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

