import numpy as np

data_file = "sample.txt"
data_file = "data.txt"

with open(data_file) as f:
    line = f.read().splitlines()[0].split(",")
    positions = np.array(line, dtype=int)

    min = np.min(positions)
    max = np.max(positions)

    min_fuel = 10000000000000000
    for pos in range(min, max + 1):
        new_positions = positions - pos
        fuel = np.abs(new_positions).sum()
        if fuel < min_fuel:
            min_fuel = fuel

    print(min_fuel)
