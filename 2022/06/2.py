from collections import deque

data_file = "sample.txt"
data_file = "data.txt"


def find_different_group(s: str, n: int) -> int:
    d = deque()
    for i, c in enumerate(s):

        if len(d) == n:
            d.popleft()
        d.append(c)

        if len(set(d)) == n:
            result = i
            break
    return result


with open(data_file) as f:
    lines = f.read().splitlines()

    for l in lines:
        m = find_different_group(l, 14)
        print(m + 1)
