# S = (P x I x t / K) / 100
sum = float(input('Начальный деп: '))
bet = 4
day = 365
calendar = 365
year = 1
formula = (sum * bet * (day * year) / calendar)
print(f'За 1 год: {formula}')
god = "qqq" # почему не работаут?)
print(f'За 2 год: {formula}')
god = 3
print(f'За 3 год: {formula}')


def formula(year: int):
    print(f'За {year} год: {sum * bet * (day * year) / calendar}')


formula(1)
formula(2)
formula(3)
