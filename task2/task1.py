souvenirs = input('ведите количество сувениров')
trinkets = input('ведите количество безделух')
if souvenirs.isdigit() and trinkets.isdigit():
    souvenirs, trinkets = int(souvenirs), int(trinkets)
    print((75 * souvenirs) + (112 * trinkets))