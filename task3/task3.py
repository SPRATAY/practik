def file(file1: str):
    try:
        print(file1.split(".",1)[1])
    except:
        print('не выполнено')


file('python')