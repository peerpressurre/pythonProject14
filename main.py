def calculator():
    try:
            expression = input('enter expression using back spaces to separate each symbol->')
            list = expression.split(' ')
            length = len(list)
            intlist = map(int, list)
            num1 = expression[0]
            num2 = expression[3:]
            inted_num1 = map(int, num1)
            inted_num2 = map(int, num2)

            print(num1)
            print(num2)
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
                    division = (num1 / num2)
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