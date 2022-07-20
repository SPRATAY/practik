day = input('ведите дней')
hours = input('ведите часы')
min = input('ведите минут')
if day.isdigit() and hours.isdigit() and min.isdigit():
    day, hours, min = int(day), int(hours), int(min)
    print(f'{(day * 86400) + (hours * 3600) + (min * 60)}')
