def file(file1: str):
    try:
        w = file1.split(".")[1:]
        if w:
            return w[-1]
        raise Exception('не удалось обработать')
    except Exception as error:
        return error


print(file('........py.....hon.txt'))
print(file(' '))
print(file('0'))
print(file('text.txt'))