pedido = input().split()

for i in range(2):
    pedido[i] = int(pedido[i])


if pedido[0] == 1:
    valor = 4 * pedido[1]
    print(f"Total: R$ {valor:.2f}")
elif pedido[0] == 2:
    valor = 4.5 * pedido[1]
    print(f"Total: R$ {valor:.2f}")
elif pedido[0] == 3:
    valor = 5 * pedido[1]
    print(f"Total: R$ {valor:.2f}")
elif pedido[0] == 4:
    valor = 2 * pedido[1]
    print(f"Total: R$ {valor:.2f}")
elif pedido[0] == 5:
    valor = 1.5 * pedido[1]
    print(f"Total: R$ {valor:.2f}")