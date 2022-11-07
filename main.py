def add():
    try:
        num = int(input('Enter a number->'))
        ones = []
        tens = []
        hundreds = []
        thousands = []
        for i in range(0, num + 1):
            ones.append(i)

        for i in range(0, num + 1):
            if i % 10 == 0:
                tens.append(i)

        for i in range(0, num + 1):
            if i % 100 == 0:
                hundreds.append(i)

        for i in range(0, num + 1):
            if i % 1000 == 0:
                thousands.append(i)
        print(f'Ones: {ones}\nTens: {tens}\nHundreds: {hundreds}\nThousands: {thousands}')



    except Exception as ex:
        print(f'Error: {ex}')
add()