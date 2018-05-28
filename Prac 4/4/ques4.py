# Adds students and list of their spoken lang to dict
no_of_stud = int(input("no of stud: "))
d = dict()

while no_of_stud > 0:
    no_of_stud -=1
    stu = input("name of student: ")
    no_lang = int(input("number of languages spoken: "))
    lang = []
    x = 1
    while no_lang > 0:
        no_lang -=1
        lang.append(input("language {}: ".format(x)))
        x += 1
    d[stu] = lang


# Finds no of languages
n = set()
for i in d:
    for j in d[i]:
        n.add(j)
print("Number of languages = {} ".format(len(n)))

# sorted in alphabetical order
lst = sorted(n)
for i in lst:
    print(i)
