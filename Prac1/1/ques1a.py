prev = 0
curr = 1
print(prev, curr, end=" ")
for i in range(3, 21):
    nex = prev + curr
    prev = curr
    curr = nex
    print(nex, end=" ")