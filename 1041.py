x, y = input().split(" ")

x = float(x)
y = float(y)

first_quadrant = x > 0 and y > 0
second_quadrant = x < 0 and y > 0
third_quadrant = x < 0 and y < 0
fourth_quadrant = x > 0 and y < 0
origin = x == 0 and y == 0
y_axis = x != 0 and y == 0
x_axis = x == 0 and y != 0

if first_quadrant:
    print("Q1")
elif second_quadrant:
    print("Q2")
elif third_quadrant:
    print("Q3")
elif fourth_quadrant:
    print("Q4")
elif origin:
    print("Origem")
elif x_axis:
    print("Eixo X")
elif y_axis:
    print("Eixo Y")