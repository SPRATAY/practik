"""
Расстояние. Для этого упражнения вам необходимо будет написать
программу, которая будет запрашивать у пользователя расстояние в футах. После этого
она должна будет пересчитать это число в дюймы, ярды и мили и вывести на экран.
Коэффициенты для пересчета единиц вы без труда найдете в интернете
1futi 2futi>duimi and yardi and mili
"""
futi = float(input('ведите футы'))
# if futi.isdigit
print(f'дюймы: {futi * 12}')
print(f'ярды: {futi * 0.33333234018318}')
print(f'мили: {futi * 0.00018939387935758}')
