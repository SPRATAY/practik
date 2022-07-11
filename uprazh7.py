# S = (P x I x t / K) / 100
summa = float(input('Начальный деп: '))
stavka = 4
dney = 365
kalendar = 365
god = 1
formyla = (summa * stavka * (dney * god) / kalendar)
print(f'За 1 год: {formyla}')
god = "qqq"
print(f'За 2 год: {formyla}')
god = 3
print(f'За 3 год: {formyla}')
# непонял пытаюсь сделать


def formyla(god):
    print(f'За {god} год: {summa * stavka * (dney * god) / kalendar}')


formyla(1)
formyla(2)
formyla(3)
