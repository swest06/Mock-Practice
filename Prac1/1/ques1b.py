n = 2000
prev = 0
curr = 1
c = 0
print(prev, curr, end=" ")
while prev + curr < n:
    print(prev + curr, end=" ")
    nex = prev + curr
    prev = curr
    curr = nex
    c +=1
print("")
print(c)