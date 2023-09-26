divisor = int(input())

for i in range(1, 10001):
    if (i % divisor) == 2:
        print(i)