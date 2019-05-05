# def spesum(*params):
#     params = reversed(params)
#     if params[0] == 5:
#         summ = sum(params)
#         print(summ*5)
#     else:
#         print(summ*3)
#
#
# spesum(1,5,6,8,5)

def  finDafodnum():
    for num in range(100, 1000):
        while num:
            z = 0
            z += num%10
            num = num //10
    return z
print(finDafodnum())