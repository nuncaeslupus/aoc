import numpy as np

data_file = "sample.txt"
data_file = "data.txt"

with open(data_file) as f:
    line = f.read().splitlines()[0].split(",")
    positions = np.array(line, dtype=int)

    min = np.min(positions)
    max = np.max(positions)

    min_fuel = np.iinfo(np.int64).max
    for pos in range(min, max + 1):
        new_positions = positions - pos
        fuel = (np.abs(new_positions) * (np.abs(new_positions) + 1) / 2).sum()
        if fuel < min_fuel:
            min_fuel = fuel

    print(int(min_fuel))
