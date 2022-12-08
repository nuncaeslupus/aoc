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
    td, tu, tr, tl = (t_bool.copy(True) for i in range(4))

    table_cols = pd.DataFrame([range(height)] * height)
    table_rows = table_cols.transpose()

    t_zeros = pd.DataFrame(np.zeros_like(table))
    td_count, tu_count, tr_count, tl_count = (t_zeros.copy(True) for i in range(4))

    for i in range(1, height):
        td_ge = np.greater_equal(
            table,
            table.combine(table_add.shift(i, axis=0, fill_value=-1), np.maximum),
        )
        td_count[td & (~td_ge | (table_rows > i - 1))] += 1
        td = td & td_ge

        tu_ge = np.greater_equal(
            table,
            table.combine(table_add.shift(-i, axis=0, fill_value=-1), np.maximum),
        )
        tu_count[tu & (~tu_ge | (table_rows <= height - i - 1))] += 1
        tu = tu & tu_ge

    for i in range(1, width):
        tr_ge = np.greater_equal(
            table,
            table.combine(table_add.shift(i, axis=1, fill_value=-1), np.maximum),
        )
        tr_count[tr & (~tr_ge | (table_cols > i - 1))] += 1
        tr = tr & tr_ge

        tl_ge = np.greater_equal(
            table,
            table.combine(table_add.shift(-i, axis=1, fill_value=-1), np.maximum),
        )
        tl_count[tl & (~tl_ge | (table_cols <= width - i - 1))] += 1
        tl = tl & tl_ge

    table_trees = td_count * tu_count * tr_count * tl_count
    result = table_trees.max().max()
    print(result)

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
