bred = 3.49
sale = 0.60
sbred = bred * sale
buy = ('Сколько купить вчерашнего хлеба?')
if buy.isdigit():
    buy = int(buy)
    print(f'цена хлеба: {bred}')
    print(f'цена вчеращнего хлеба: {round(sbred, 2)}')
    print(f'цена приобритеного хлеба: {round(sbred * int(buy), 2)}')
