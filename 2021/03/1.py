import numpy as np
import pandas as pd

data_file = "sample.txt"
data_file = "data.txt"

with open(data_file) as f:
    lines = f.read().splitlines()
    table = np.array([list(l) for l in lines])
    df = pd.DataFrame(table)
    gamma = "".join(df.mode(axis=0).values[0])
    epsilon = gamma.replace("1", "2").replace("0", "1").replace("2", "0")

    result = int(gamma, 2) * int(epsilon, 2)
    print(result)
