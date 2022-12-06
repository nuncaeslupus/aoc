import pandas as pd
import numpy as np
from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()

    table = pd.DataFrame()
    for l in lines:

        row = pd.Series(([c for c in l])).astype(np.int64)
        table = pd.concat((table, row), axis=1)

    table = table.transpose()
    td = table.shift(1).replace(np.nan, np.iinfo(np.int64).max)
    tu = table.shift(-1).replace(np.nan, np.iinfo(np.int64).max)
    tr = table.shift(1, axis=1).replace(np.nan, np.iinfo(np.int64).max)
    tl = table.shift(-1, axis=1).replace(np.nan, np.iinfo(np.int64).max)

    low_mask = (td - table > 0) & (tu - table > 0) & (tr - table > 0) & (tl - table > 0)
    low = table.mask(~low_mask)

    result = int((low + 1).sum().sum())
    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
