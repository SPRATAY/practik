"""
Упражнение 4. Площадь садового участка. Создайте программу, запрашивающую
у пользователя длину и ширину садового участка в футах. Выведите на экран площадь
участка в акрах. Подсказка. В одном акре содержится 43 560 квадратных футов
(fdlina + fshirina)/ 43 560 = result
"""
fdlina = float(input('укажите длину:'))
fshirina = float(input('укажите ширину:'))
# if fdlina.is_n() and fshirina.isdigit():
print((fdlina + fshirina) // 43.500)