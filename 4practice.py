"""
Упражнение 4. Площадь садового участка. Создайте программу, запрашивающую
у пользователя длину и ширину садового участка в футах. Выведите на экран площадь
участка в акрах. Подсказка. В одном акре содержится 43 560 квадратных футов
(fdlina + fshirina)/ 43 560 = result
"""
ftlength = input('укажите длину:')
ftwidth = input('укажите ширину:')
if ftlength.isdigit() and ftwidth.isdigit():
    ftlength, ftwidth = float(ftlength), float(ftwidth)
    print((ftlength + ftwidth) // 43.500)
