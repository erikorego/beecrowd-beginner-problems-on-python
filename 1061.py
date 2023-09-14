dia_inicio = input().lstrip("Dia ")
tempo_inicio = input().split(" : ")
dia_fim = input().lstrip("Dia ")
tempo_fim = input().split(" : ")

def tempo_em_segundos(horas, minutos, segundos):
    horas_em_minutos = horas * 60
    minutos_total = horas_em_minutos + minutos
    minutos_em_segundos = minutos_total * 60
    tempo_em_segundos = minutos_em_segundos + segundos
    return tempo_em_segundos

def tempo_normal(segundos):
    minutos = segundos // 60
    segundos %= 60
    horas = minutos // 60
    minutos %= 60
    dias = horas // 24
    horas %= 24
    return dias, horas, minutos, segundos

dia_inicio, dia_fim = int(dia_inicio), int(dia_fim)
for i in range(3):
    tempo_inicio[i] = int(tempo_inicio[i])
    tempo_fim[i] = int(tempo_fim[i])


tempo_total_segundos = tempo_em_segundos((dia_fim-dia_inicio-1)*24, 0, 0)

tempo_primeiro_dia = tempo_em_segundos(24, 0, 0) - tempo_em_segundos(tempo_inicio[0], tempo_inicio[1], tempo_inicio[2])
tempo_segundo_dia = tempo_em_segundos(tempo_fim[0], tempo_fim[1], tempo_fim[2])
tempo_total_segundos += tempo_primeiro_dia + tempo_segundo_dia

tempo_total = tempo_normal(tempo_total_segundos)
print(f"{tempo_total[0]} dia(s)\n{tempo_total[1]} hora(s)\n{tempo_total[2]} minuto(s)\n{tempo_total[3]} segundo(s)")