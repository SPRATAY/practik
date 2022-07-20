number1 = input('1 число')
number2 = input('2 число')
number3 = input('3 число')
if number1.isdigit() and number2.isdigit() and number3.isdigit():
    number1, number2, number3 = int(number1), int(number2), int(number3)
    sort = [number1, number2, number3]
    sort.sort()
    print(sort)
