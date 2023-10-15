while True:
    numeros = input().split(" ")
    x = int(numeros[0])
    y = int(numeros[1])
    if x == y:
        break
    else:
        if x < y:
            print("Crescente")
        else:
            print("Decrescente")