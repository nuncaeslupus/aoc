import re
from collections import defaultdict
from math import prod
from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

start = timer()
board: list[list[str]] = []


def is_symbol(s: str) -> bool:
    return s == "*"


# Read
with open(data_file, encoding="utf-8") as f:
    for l in f.read().splitlines():
        board.append(list(l))

width = len(board[0])
height = len(board)

board_aux: list[list[set[int]]] = [[set() for _ in range(width)] for _ in range(height)]
symbols: list[list[int]] = [[-1 for _ in range(width)] for _ in range(height)]

# Count symbols
num_symbols = 0
for i in range(height):
    for j in range(width):
        if is_symbol(board[i][j]):
            symbols[i][j] = num_symbols
            num_symbols += 1

counts = [0 for _ in range(num_symbols)]

# Assign symbol numbers to numbers
for i in range(height):
    for j in range(width):
        if is_symbol(board[i][j]):
            symbol_num = symbols[i][j]

            ul = uc = ur = cl = cr = dl = dc = dr = -1

            if not i == 0 and not j == 0 and board[i - 1][j - 1].isdigit():
                ul = symbol_num
                board_aux[i - 1][j - 1].add(ul)

            if not i == 0 and board[i - 1][j].isdigit():
                uc = symbol_num
                board_aux[i - 1][j].add(uc)

            if not i == 0 and not j == width - 1 and board[i - 1][j + 1].isdigit():
                ur = symbol_num
                board_aux[i - 1][j + 1].add(ur)

            if not j == 0 and board[i][j - 1].isdigit():
                cl = symbol_num
                board_aux[i][j - 1].add(cl)

            if not j == width - 1 and board[i][j + 1].isdigit():
                cr = symbol_num
                board_aux[i][j + 1].add(cr)

            if not i == height - 1 and not j == 0 and board[i + 1][j - 1].isdigit():
                dl = symbol_num
                board_aux[i + 1][j - 1].add(dl)

            if not i == height - 1 and board[i + 1][j].isdigit():
                dc = symbol_num
                board_aux[i + 1][j].add(dc)

            if (
                not i == height - 1
                and not j == width - 1
                and board[i + 1][j + 1].isdigit()
            ):
                dr = symbol_num
                board_aux[i + 1][j + 1].add(dr)

            count = 0
            if ul == symbol_num or uc == symbol_num or ur == symbol_num:
                if uc == symbol_num:
                    count += 1
                elif ul == symbol_num and ur == symbol_num:
                    count += 2
                else:
                    count += 1
            if cl == symbol_num:
                count += 1
            if cr == symbol_num:
                count += 1
            if dl == symbol_num or dc == symbol_num or dr == symbol_num:
                if dc == symbol_num:
                    count += 1
                elif dl == symbol_num and dr == symbol_num:
                    count += 2
                else:
                    count += 1
            counts[symbol_num] = count

# Find only wanted (exactly 2)
wanted = [i for i in range(num_symbols) if counts[i] == 2]

# Expand symbol numbers through neighbor numbers
for i in range(height):
    for j in range(width):
        wanted_list = []
        for s in board_aux[i][j]:
            if s in wanted:
                wanted_list.append(s)
        board_aux[i][j] = set(wanted_list)

        for s in board_aux[i][j]:
            end_left = False
            p = 1
            while not end_left and j - p != -1:
                if board[i][j - p].isdigit():
                    board_aux[i][j - p].add(s)
                    p += 1
                else:
                    end_left = True

            end_right = False
            p = 1
            while not end_right and j + p != width:
                if board[i][j + p].isdigit():
                    board_aux[i][j + p].add(s)
                    p += 1
                else:
                    end_right = True

board_aux_2: list[list[str]] = [[" " for _ in range(width)] for _ in range(height)]
for i in range(height):
    for j in range(width):
        if board_aux[i][j] == set():
            board[i][j] = " "
        else:
            if j == 0 or board_aux[i][j - 1] != board_aux[i][j]:
                board_aux_2[i][j] = f"{board_aux[i][j]}"

result: defaultdict[int, list[int]] = defaultdict(list)
for i, l in enumerate(board):
    string = "".join(l)
    string_aux = "".join(el[1:-1] if el[0] == "{" else el for el in board_aux_2[i])
    numbers = re.findall(r"(\d+)", string)
    symb = re.findall(r"(\d+)", string_aux)
    for n, number in enumerate(numbers):
        result[int(symb[n])].append(int(number))

print(f"Result: {sum([prod(values) for values in result.values()])}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
