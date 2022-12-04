import numpy as np

data_file = "sample.txt"
data_file = "data.txt"

days = 80

with open(data_file) as f:
    line = f.read().splitlines()[0].split(",")
    timers = np.array(line, dtype=int)

    for day in range(days):
        timers -= 1
        negative = timers == -1
        timers[negative] = 6
        timers = np.append(timers, np.ones(np.count_nonzero(negative), dtype=int) * 8)
    result = len(timers)
    print(result)
