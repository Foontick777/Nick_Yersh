num = input('enter num: ').split()
def decorator(func):
    def wrapper(*data):
        list = []
        for i in func(data):
            if int(i) % 2 == 0:
                list.append(i)
        print(list)
        return func(data)
    return wrapper


@decorator
def lst(spis):
    for i in spis:
        return i

lst(num)