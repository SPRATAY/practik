"""
Цельсий в Фаренгейт и Кельвин. Напишите программу, которая будет
запрашивать у пользователя значение температуры в градусах Цельсия и отображать
эквивалентный показатель по шкалам Фаренгейта и Кельвина. Необходимые
коэффициенты и формулы для проведения расчетов нетрудно найти на просторах
интернета
"""
c = input('сколько градусов цельсия: ')
if c.isdigit():
    c = float(c)
    print(f'фаренгейт: {(c * 1.8) + 32}')
    print(f'кельвин: {c + 273.15}')
