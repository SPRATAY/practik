fytii = input('ведите футы: ')
duim = input('ведите дюймы; ')
if fytii.isdigit() and duim.isdigit():
    print(((float(fytii) * 12) * 2.54) + (float(duim) * 2.54))
