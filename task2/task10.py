my_list = []

while True:
    x = int(input('Ведите цыфры:'))
    if x == 0:
        print('Вышел')
        break

    my_list.append(x)
print(my_list)