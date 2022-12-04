import numpy as np

data_file = "sample.txt"
data_file = "data.txt"

days = 256

with open(data_file) as f:
    line = f.read().splitlines()[0].split(",")
    timers = np.array(line, dtype=int)

    values = range(0, 9)
    unique, counts = np.unique(timers, return_counts=True)
    counters = np.array([0] * 9)
    for val in values:
        pos = np.where(unique == val)[0]
        if pos.size > 0:
            counters[val] = counts[pos]

    for day in range(days):
        negative = counters[0]
        counters = np.roll(counters, -1)
        counters[6] += negative
    result = counters.sum()
    print(result)
