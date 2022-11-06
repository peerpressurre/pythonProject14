def calculator():
    try:
            expression = input('enter expression using back spaces to separate each symbol->')
            list = expression.split(' ')
            print(list)
            length = len(list)
            intlist = map(int, list)
            num1 = list[0]
            num2 = list[2:]
            print(f'num1: {num1}')
            print(f'num2: {num2}')

            # inted_num1 = map(int, num1)
            # print(inted_num1)
            inted_num2 = map(int, num2)
            print(f'int: {inted_num2}')


            nums = []
            for i in list:
                if i.isdigit() == True:
                    nums.append(i)
            inted_nums = map(int, nums)
            if 0 < length < 4:
                if list.count('+') > 0:
                    summary = sum(inted_nums)
                    print(summary)
                if list.count('-') > 0:
                    division = (inted_num1 - inted_num2)
                    print(division)
                if list.count('*') > 0:
                    product = intlist[:1] * intlist[1:]
                    print(product)
                if list.count('/') > 0:
                    fraction = intlist[:1] / intlist[1:]
                    print(fraction)
            else:
                print('Error: Expression can only contain of 3 symbols')







    except Exception as ex:
        print(f'Error: {ex}')
calculator()