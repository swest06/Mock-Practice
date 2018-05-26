def main():

    lst2 = [1, 2, 3, 4]

    n = int(input("number of lines"))

    for i in range(0, n):
        txt = input()
        lst = txt.split()
        print(lst)


if __name__ == '__main__':
    main()

