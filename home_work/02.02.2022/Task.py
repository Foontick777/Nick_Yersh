def main():
    lst = [str(input(f'enter word №{i + 1}: ')) for i in range(3)]
    print('Word(s) palindrome: ', *[a for a in lst if str(a) == str(a[::-1])])

if __name__ == '__main__':
    main()




