valores = [float(input()) for i in range(6)]
positivos = [valor for valor in valores if valor > 0]
print(f'{len(positivos)} valores positivos')
media = sum(positivos) / len(positivos)
print(f'{media:.1f}')