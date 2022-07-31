my_list = []

while True:
    s = input('ведите слова')
    if s == '':
        print('Вышел')
        break

    my_list.append(s)
print(list(dict.fromkeys(my_list)))
