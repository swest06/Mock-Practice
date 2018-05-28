n = int(input("how many lines: "))
txt = []
l = 1

# Adds words in line to list
while n > 0:
    line = str(input("line {}: ".format(l)))
    a = line.split()
    for i in a:
        txt.append(i)
    n -= 1
    l += 1

# Sorts words in alphabetical order
y = sorted(txt)
# Sorts words in descending order of occurrence
x = sorted(y, key=y.count, reverse=True)

# Prints words (doesn't repeat same word twice)
print(x[0])
j = x[0]
for i in x:
    if i != j:
        print(i)
        j = i
