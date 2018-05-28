# Takes a number and determines if it is prime
n = int(input("Type number: "))
prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False
print(prime)




# Prints all prime numbers in range
for i in range(2, 100):
    prime2 = True
    for j in range(2, i):
        if i % j == 0:
            prime2 = False
    if prime2:
        print(i)