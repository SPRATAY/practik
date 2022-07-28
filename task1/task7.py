# (7 * nedela) + (30 * mesats) + (365 * year)
tom = input('Ведите неделю: ')
mon = input('ведите месяц: ')
yer = input('ведите год: ')
if tom.isdigit() and mon.isdigit() and yer.isdigit():
    tom, mon, yer = int(tom), int(mon), int(yer)
    print(7 * tom + 30 * mon + 365 * yer)
