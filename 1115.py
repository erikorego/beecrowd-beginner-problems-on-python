while True:
    
    x, y = input().split(" ")
    x, y = int(x), int(y)

    quadrante_um = x > 0 and y > 0
    quadrante_dois = x < 0 and y > 0
    quadrante_tres = x < 0 and y < 0
    quadrante_quatro = x > 0 and y < 0

    if x == 0 or y == 0:
        break
    elif quadrante_um:
        print("primeiro")
    elif quadrante_dois:
        print("segundo")
    elif quadrante_tres:
        print("terceiro")
    elif quadrante_quatro:
        print("quarto")