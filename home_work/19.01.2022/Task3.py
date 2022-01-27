def factor(num):
    if num == 0:
        return 1
    return factor(num-1)*num
x = input('enter num: ')
print(factor(int(x)))
