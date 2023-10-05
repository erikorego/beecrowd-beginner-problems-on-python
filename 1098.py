i = [round(x * 0.2, 1) if x * 0.2 not in [0,1,2] else round(x * 0.2) for x in range(11)]

for valor in i:
    for j in range(1, 4):
        print(f"I={valor} J={j + valor}")