import re
import pandas as pd
import numpy as np

data_file = "sample.txt"
data_file = "data.txt"

with open(data_file) as f:
    lines = f.read().splitlines()

    width = 0
    height = 0

    vents: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for l in lines:
        coords = re.search("(\d*),(\d*) -> (\d*),(\d*)", l)
        c0 = int(coords.group(1)), int(coords.group(2))
        c1 = int(coords.group(3)), int(coords.group(4))
        vents.append((c0, c1))
        width = max(max(c0[0], c1[0]) + 1, width)
        height = max(max(c0[1], c1[1]) + 1, height)

    df = pd.DataFrame(np.zeros((height, width), dtype=int))
    for c0, c1 in vents:
        min_x = min(c0[0], c1[0])
        max_x = max(c0[0], c1[0]) + 1
        min_y = min(c0[1], c1[1])
        max_y = max(c0[1], c1[1]) + 1
        if c0[0] == c1[0] and c0[1] != c1[1]:
            for i in range(min_y, max_y):
                df.iloc[i, c0[0]] += 1
        elif c0[1] == c1[1] and c0[0] != c1[0]:
            for i in range(min_x, max_x):
                df.iloc[c0[1], i] += 1
        else:
            sign_x = np.sign(c1[0] - c0[0]) or 1
            sign_y = np.sign(c1[1] - c0[1]) or 1
            for i in range(max_x - min_x):
                df.iloc[
                    min_y + i if sign_x == sign_y else max_y - i - 1, min_x + i
                ] += 1

    result = (df > 1).sum().sum()
    print(result)
