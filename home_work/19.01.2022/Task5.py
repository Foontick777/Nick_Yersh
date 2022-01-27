def su(*data):
    s = 0
    for i in range(len(data)):
        s = s + i * int(data[i])
    return s
num = input('enter num: ').split()
print(su(*num))