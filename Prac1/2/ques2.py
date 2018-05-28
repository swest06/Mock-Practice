def search(str, lst, size):
    for i in range(0, size):
        if str == lst[i]:
            return i
    return -1


lst = ["hello", "my", "name", "is", "sean"]
print(search(input("string: "), lst, 5))