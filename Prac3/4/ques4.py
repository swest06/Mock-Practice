def fib(n):
    prev = 0
    curr = 1
    print(prev, end=" ")
    print(curr, end=" ")
    while n - 2 > 0:
        nex = prev + curr
        print(nex, end= " ")
        prev = curr
        curr = nex
        n -=1

n = int(input("num: "))
fib(n)


def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)