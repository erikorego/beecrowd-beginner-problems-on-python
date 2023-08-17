numeros = input().split(" ")

maior = (int(numeros[0]) + int(numeros[1]) + abs(int(numeros[0])-int(numeros[1]))) / 2
maior = (maior + int(numeros[2]) + abs(maior-int(numeros[2]))) / 2

print(f"{maior:.0f} eh o maior")