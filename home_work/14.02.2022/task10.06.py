with open('test1.txt', 'r') as my_file1:
    l1 = my_file1.readlines()
with open('test2.txt', 'r') as my_file2:
    l2 = my_file2.readlines()
for i in range(len(l2)):
    if l1[i] == l2[i]:
        print(f'{i + 1} строка совпадает')
    else:
        print(f'{i + 1} строка не совпадает')



def get(line1: str, line2: str):
    return ','.join(set(line1.split()) - set(line2.split()))

with open('test1.txt') as my_file1, open('test2.txt') as my_file2:
    lst = list(zip(my_file1.readlines(), my_file2.readlines()))
    for i in lst:
        l1 = i[0].rstrip()
        l2 = i[1].rstrip()
        if l1 != l2:
            print(f'"{l1}" не равно "{l2}"!\n Символы в строке которые не совпадают: {get(l1, l2)}\n')
