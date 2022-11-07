def dududu():
   try:
       nums = (input('enter numbers->'))
       split_list = nums.split(' ')
       inted_list =[eval(i) for i in split_list]
       negative = []
       positive = []
       print(f'Max number is: {max(inted_list)}\nMin number is: {min(inted_list)}')
       for i in inted_list:
            if i > 0:
                positive.append(i)
            if i < 0:
               negative.append(i)
       print(f'positive numbers are: {positive}\nNegative numbers are: {negative}')


   except Exception as ex:
        print(f'Error: {ex}')
dududu()