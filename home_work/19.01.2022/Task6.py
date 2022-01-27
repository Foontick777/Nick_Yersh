def summ(*data):
    s = 0
    for i in data:
        s = s + int(i)
    return f'Sum: {s}, Max: {max(data)}'
num = input('enter: ').split()
print(summ(*num))