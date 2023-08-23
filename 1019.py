tempo_segundos = int(input())

tempo_minutos = tempo_segundos // 60
tempo_segundos %= 60

tempo_horas = tempo_minutos // 60
tempo_minutos %= 60

print(f"{tempo_horas}:{tempo_minutos}:{tempo_segundos}")