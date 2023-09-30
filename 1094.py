numero_testes = int(input())

coelhos = 0
ratos = 0
sapos = 0

for i in range(numero_testes):
    teste = input().split(" ")
    if teste[1] == "C":
        coelhos += int(teste[0])
    elif teste[1] == "R":
        ratos += int(teste[0])
    elif teste[1] == "S":
        sapos += int(teste[0])

cobaias = ratos + sapos + coelhos

def percentual (parte, todo):
    valor_percentual = (parte / todo) * 100
    return valor_percentual

print(f"Total: {cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual(coelhos, cobaias):.2f} %")
print(f"Percentual de ratos: {percentual(ratos, cobaias):.2f} %")
print(f"Percentual de sapos: {percentual(sapos, cobaias):.2f} %")