my_list = []

while True:
    x = int(input('Ведите цыфры:'))
    if x == 0:
        print('Вышел')

    my_list.append(x)
print(sorted(my_list))
