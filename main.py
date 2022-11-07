def calc():
    try:
        ex = input("Введіть приклад: ")
        if ex.find('+') != -1:
            n = ex.find('+')
            print(float(ex[:n]) + float(ex[n + 1:len(ex)]))
        if ex.find('-') != -1:
            n = ex.find('-')
            print(float(ex[:n]) - float(ex[n + 1:len(ex)]))
        if ex.find('*') != -1:
            n = ex.find('*')
            print(float(ex[:n]) * float(ex[n + 1:len(ex)]))
        if ex.find('/') != -1:
            n = ex.find('/')
            print(float(ex[:n]) / float(ex[n + 1:len(ex)]))

    except Exception as ex:
        print(f'Error: {ex}')

calc()
