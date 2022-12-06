from collections import deque

data_file = "sample.txt"
data_file = "data.txt"

with open(data_file) as f:
    lines = f.read().splitlines()

    for l in lines:
        result = None
        d = deque()
        for i, c in enumerate(l):
            if len(d) == 4:
                d.popleft()
            d.append(c)

            if len(set(d)) == 4:
                result = i
                break
        print(result + 1)
