def Narci():
    for each in range(100, 1000):
        temp = each
        summ = 0
        while temp:
            summ = summ + (temp % 10) ** 3
            temp = temp // 10

        if  summ == each:
            print(each, end='\t')


Narci()