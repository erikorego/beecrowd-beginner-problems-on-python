valores = input().split(" ")

for i in range(len(valores)):
    valores[i] = int(valores[i])

hora_inicio = valores[0]
minuto_inicio = valores[1]

hora_fim = valores[2]
minuto_fim = valores[3]

if (hora_fim < hora_inicio) or (hora_fim == hora_inicio and minuto_fim == minuto_inicio):
    hora_fim += 24

total_minutos_inicio = (hora_inicio * 60) + minuto_inicio
total_minutos_fim = (hora_fim * 60) + minuto_fim

duracao_minutos = total_minutos_fim - total_minutos_inicio
duracao_horas = duracao_minutos // 60
duracao_minutos %= 60
if duracao_horas < 0:
    duracao_horas += 24

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")