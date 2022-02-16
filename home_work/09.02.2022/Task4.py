def decorator(func):
    def wrapper(*data):
        data = func(*data[::-1])
        return func(*data)
    return wrapper

@decorator
def func(*data):
    return data

num = input('enter: ').split()
print(func(*num))