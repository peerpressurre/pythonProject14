def calc():
    try:
        ex = (input('enter expression using back spaces to separate each symbol->'))
        ex_split = ex.split(' ')
        print(ex_split)
        length = len(ex_split)
        intlist = [eval(i) for i in ex_split]
        print(f'inted: {intlist}')


        nums = []
        for i in list:
            if i.isdigit() == True:
                nums.append(i)
        num1 = nums[0]
        num2 = nums[2:]
        print(f'num1: {num1}')
        print(f'num2: {num2}')

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

calc()
