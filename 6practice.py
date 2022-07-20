souvenirs = input('ведите количество сувениров')
trinkets = input('ведите количество безделух')
if souvenirs.isdigit() and trinkets.isdigit():
    print((75 * int(souvenirs)) + (112 * int(trinkets)))
