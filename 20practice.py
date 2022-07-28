#'31 день': ['январь', 'март', 'май', 'июль', 'август', 'октябырь', 'декабырь'],

month = 'май'
days_of_month = {
    '31 день': ['январь', 'март', 'май', 'июль', 'август', 'октябырь', 'декабырь'],
    '30 дней': ['апрель', 'июнь', 'ноябырь'],
    '29 или 28 дней': ['февраль'],
}
#print(days_of_month['31 день'])
#days_of_monthfor value in days_of_month['31 день']:
print(f'{month.capitalize()} содержит {days_of_month.get(month.lower(), "не найден")}')
#print(days_of_month.get(month.lower(), 'не найден'))
#for value in days_of_month:
#    if month.lower() in days_of_month[value]:
#        print(f'{month.capitalize()} содержит {value}')
#        break
#else:
#    print(f'{month.capitalize()} не найден')