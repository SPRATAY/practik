ft = input('ведите футы: ')
inch = input('ведите дюймы; ')
if ft.isdigit() and inch.isdigit():
    print(((float(ft) * 12) * 2.54) + (float(inch) * 2.54))
