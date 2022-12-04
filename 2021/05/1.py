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
        if c0[0] == c1[0] or c0[1] == c1[1]:
            vents.append((c0, c1))
        width = max(max(c0[0], c1[0]) + 1, width)
        height = max(max(c0[1], c1[1]) + 1, height)

    df = pd.DataFrame(np.zeros((height, width), dtype=int))
    for c0, c1 in vents:
        if c0[0] == c1[0]:
            for i in range(min(c0[1], c1[1]), max(c0[1], c1[1]) + 1):
                df.iloc[i, c0[0]] += 1
        elif c0[1] == c1[1]:
            for i in range(min(c0[0], c1[0]), max(c0[0], c1[0]) + 1):
                df.iloc[c0[1], i] += 1

    result = (df > 1).sum().sum()
