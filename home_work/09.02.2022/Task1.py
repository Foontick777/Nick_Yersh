def main():
    lst = [str(input(f'enter word №{i + 1}: ')) for i in range(5)]
    lst2 = [str(lst.index(i)) + ":" + i for i in lst]
    print(*lst2)

if __name__ == '__main__':
    main()