import numpy as np

with open("data.txt") as f:
    elves = []
    sum = 0
    for l in f.readlines():
        if l != "\n":
            sum += int(l)
        else:
            elves.append(sum)
            sum = 0
    print(np.sum(sorted(elves, reverse=True)[:3]))
