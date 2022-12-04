import numpy as np
import pandas as pd

data_file = "sample.txt"
data_file = "data.txt"

with open(data_file) as f:
    lines = f.read().splitlines()

    drawn = np.array(lines[0].split(","), dtype=int)
    boards: list[pd.DataFrame] = []
    for i in range(2, len(lines), 6):
        board = [np.array(row.split(), dtype=int) for row in lines[i : i + 5]]
        df = pd.DataFrame(board)
        boards.append(df)

    losers = list(range(len(boards)))

    d = None
    winner = None
    for d in drawn:
        for i, df in enumerate(boards):
            df.mask(df == d, -1, inplace=True)
            if i in losers and (
                (df.sum(axis=0) == -5).any() or (df.sum(axis=1) == -5).any()
            ):
                if len(losers) == 1:
                    winner = df
                    break
                else:
                    losers.remove(i)
        if winner is not None:
            break

    score = int(winner.replace(-1, np.NaN).sum().sum())
    result = d * score
    print(result)
