money = float(input('счет: '))
chai = 0.18
nalog = 0.20
mchai = money * chai
mnalog = money * nalog
# if money.isdigit():
print(f'чай: {mchai}')
print(f'налог: {mnalog}')
print(f'чай и налог: {mchai + mnalog}')
