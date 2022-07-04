suvenir = input('ведите количество сувениров')
bezdeluh = input('ведите количество безделух')
if bezdeluh.isdigit() and suvenir.isdigit():
    print((75 * int(suvenir)) + (112 * int(bezdeluh)))
