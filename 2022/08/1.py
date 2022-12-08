from timeit import default_timer as timer

import numpy as np
import pandas as pd

data_file = "sample.txt"
data_file = "data.txt"

start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()
    table = pd.DataFrame()
    for l in lines:
        row = pd.Series(([c for c in l])).astype(np.int64)
        table = pd.concat([table, row], axis=1)

    table = table.transpose().reset_index(drop=True)
    height, width = table.shape

    table_add = table + 1
    t_bool = pd.DataFrame(np.ones_like(table).astype(bool))
    td, tu, tr, tl = (t_bool.copy(True),) * 4

    for i in range(1, height):
        td = td & np.greater_equal(
            table,
            table.combine(table_add.shift(i, axis=0, fill_value=-1), np.maximum),
        )
        tu = tu & np.greater_equal(
            table,
            table.combine(table_add.shift(-i, axis=0, fill_value=-1), np.maximum),
        )
    for i in range(1, width):
        tr = tr & np.greater_equal(
            table,
            table.combine(table_add.shift(i, axis=1, fill_value=-1), np.maximum),
        )
        tl = tl & np.greater_equal(
            table,
            table.combine(table_add.shift(-i, axis=1, fill_value=-1), np.maximum),
        )

    table_min = td | tu | tr | tl
    result = table_min.sum().sum()
    print(result)

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
