def sum(dat):
    x = 0
    while dat:
        a = input('enter: ')
        if a == "exit":
            return x
        x = x + int(a)
        print(x)


def mult(data):
    l = 1
    while data:
        b = input('enter: ')
        if b == "exit":
            return l
        l = l * int(b)
        print(l)


def res(type):
    if type == "+":
        return sum(type)
    elif type == '*':
        return mult(type)

num = input("+/*: ")
print(res(num))