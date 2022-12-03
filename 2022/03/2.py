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
    for i in range(0, len(lines), 3):
        first = set(lines[i])
        second = set(lines[i + 1])
        third = set(lines[i + 2])

        common = next(iter(first.intersection(second, third)))
        sum += get_priority(common)
    print(sum)
