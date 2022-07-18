hage = int(input("ведите возраст собаки"))
if hage < 0:
    print("Ведите значение больше 0")
    exit()
elif hage <= 2:
    dage = hage * 10.5
else:
    dage = 21 + (hage - 2)*4
print(f'Собакин возраст {dage}')
