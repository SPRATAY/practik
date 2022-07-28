km = input('Ведите расстояние в километрах: ')
min = input('Ведите время в минутах: ')
if km.isdigit() and min.isdigit():
    km, min = int(km), int(min)
    print('(1000 * km)) / (60 * min)')
