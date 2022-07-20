day = input('ведите дней')
hours = input('ведите часы')
min = input('ведите минут')
if day.isdigit() and hours.isdigit() and min.isdigit():
    print(f'{(int(day) * 86400) + (int(hours) * 3600) + (int(min) * 60)}')
