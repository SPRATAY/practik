import math
a = input('ведите a: ')
b = input('ведите б: ')
if a.isdigit() and b.isdigit():
    a, b = int(a), int(b)
    print(f'сумма a и b: {a + b}')
    print(f'разница между a и b {(a // b - 1) * 100}')
    print(f'произведение a и b: {a * b}')
    print(f'частное от деления a на b {a // b}')
    print(f'остаток от деления a на b {a % b}')
    print(math.log10(float(a)))
    print(f'результат возведения числа a в степень b {a ** b}')
