# x = 3141
# for i in input(a):
#    print(a)
# languages = ['123']
# c * 3 and for x in languages:
#    print(x)

innumber = input("ведите число")
number = [number * 1 for number in str(innumber)]
innumber = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])
print(f'{number[0]} + {number[1]} + {number[2]} + {number[3]} = {innumber}')
