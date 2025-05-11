example_array = []

x = 0

while x < 100:
    example_array.append(x)
    x += 1

for element in example_array:
    print(f'{example_array[element]}', end=',') #THIS FUCKING DOES IT
    if example_array[element] % 13 == 0:
        print('\n')