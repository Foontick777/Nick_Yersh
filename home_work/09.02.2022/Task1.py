lst = [str(input(f'enter word №{i + 1}: ')) for i in range(3)]
result = ([a for a in lst])
print("1:{}, 2:{}, 3:{}".format(*result))