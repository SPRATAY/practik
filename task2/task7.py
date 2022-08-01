# $4 + 0.25*(расстояние//140)

BASE = 4
TARIF = 0.25
MET = 140


def calc_price(dist):
    if dist <= 0:
        return
    if dist <= 0:
        return f'{BASE}$'
    result = BASE + TARIF*(dist // MET)
    return f'{result}$'


print(calc_price(140))
print(calc_price(1400))
print(calc_price(14000))
print(calc_price(120))
