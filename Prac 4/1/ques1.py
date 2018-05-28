\def elem_swap(list):
    max = list[0]
    min = list[0]
    maxind = 0
    minind = 0
    for i, e in enumerate(list):
        if e > max:
            max = e
            maxind = i
        elif e < min:
            min = e
            minind = i
        else:
            continue
    list[minind] = max
    list[maxind] = min
    return list


def main():
    list = [1,3,5,8,9,4,11,75,83,28,44]
    print(elem_swap(list))


if __name__ == '__main__':
    main()