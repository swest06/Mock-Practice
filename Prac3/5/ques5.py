a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,8,13,21,34,55]

# Intersection of lists after converted to sets
c = set(a).intersection(set(b))

# Convert to list then sort
d = sorted(list(c))

print(d)