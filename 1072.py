tests_number = int(input())

number_in = 0
number_out = 0

for i in range(tests_number):
    number = int(input())
    if number >= 10 and number <= 20:
        number_in += 1
    else:
        number_out += 1

print(number_in, 'in')
print(number_out, 'out')