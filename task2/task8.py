firs_poss = 10.95
next_poss = 2.95
poss = input('Ведите сколько посылок')
if int(poss) <= 0:
    print(f'Посылка не может быть {poss}')
elif int(poss) == 1:
    print(firs_poss)
else:
    print(firs_poss + (next_poss * (int(poss) - 1)))
