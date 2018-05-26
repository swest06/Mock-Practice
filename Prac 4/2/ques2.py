def power(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        return a*power(a, n-1)

def main():
    print(power(5, 2))

    print(1.5*1.5)
    print(power(1.5,2))
if __name__ == '__main__':
    main()