datafile = "data.txt"


def get_priority(char: str) -> int:
    ascii = ord(char)
    if ascii in range(65, 91):
        return ascii - 38
    elif ascii in range(97, 123):
        return ascii - 96
    else:
        return 0


with open(datafile) as f:
    lines = f.read().splitlines()
    sum = 0
    for l in lines:
        middle = len(l) // 2
        left = set(l[:middle])
        right = set(l[middle:])
        common = next(iter(left.intersection(right)))
        sum += get_priority(common)
    print(sum)
