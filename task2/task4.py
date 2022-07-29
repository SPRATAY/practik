number = input('ведите число')

if number.isdigit() and int(number) % 2 == 0:
    print('Чет')
else:
    print('Нечёт')