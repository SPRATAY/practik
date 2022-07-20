money = input('счет: ')
tea = 0.18
tax = 0.20
mtea = money * tea
mtax = money * tax
if money.isdigit():
    money = int(money)
    print(f'чай: {mtea}')
    print(f'налог: {mtax}')
    print(f'чай и налог: {mtea + mtax}')
