arr = (1, 2, 2)
setarr = set(arr)
if len(arr) == len(setarr):
    print("Все элементы уникальны")
else:
    print("Есть одинаковые")