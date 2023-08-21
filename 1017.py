CONSUMO = 12
tempo = int(input())
velocidade_media = int(input())

distancia = tempo * velocidade_media
combustivel_consumido = distancia/CONSUMO

print(f"{combustivel_consumido:.3f}")