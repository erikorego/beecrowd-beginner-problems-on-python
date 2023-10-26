while True:
    senha = 2002
    tentativa = int(input())

    if tentativa != senha:
        print("Senha Invalida")
    else:
        print("Acesso Permitido")
        break