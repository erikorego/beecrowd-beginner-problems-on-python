valores = input().split(" ")

inicio = int(valores[0])
fim = int(valores[1])

duracao = fim - inicio

if fim <= inicio:
    duracao = (fim + 24) - inicio
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    print(f"O JOGO DUROU {duracao} HORA(S)")
