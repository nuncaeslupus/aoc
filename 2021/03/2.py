import numpy as np
import pandas as pd

data_file = "sample.txt"
data_file = "data.txt"


def drop_rows(df: pd.DataFrame, o2: bool) -> pd.DataFrame:
    for i in range(len(df.iloc[0, :])):
        mode_i = df.iloc[:, i].mode()
        if len(mode_i) > 1:
            mode = mode_i[1]
        else:
            mode = mode_i[0]
        if not o2:
            mode = "1" if mode == "0" else "0"

        df = df.drop(df[df[i] != mode].index, axis=0)
        if df.shape[0] == 1:
            return df
    return df


with open(data_file) as f:
    lines = f.read().splitlines()
    table = np.array([list(l) for l in lines])
    df = pd.DataFrame(table)

    df_o2 = df.copy(True)
    df_co2 = df.copy(True)

    df_o2 = drop_rows(df_o2, True)
    df_co2 = drop_rows(df_co2, False)

    o2 = "".join(df_o2.mode(axis=0).values[0])
    co2 = "".join(df_co2.mode(axis=0).values[0])

    result = int(o2, 2) * int(co2, 2)
    print(result)
