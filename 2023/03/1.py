import re
from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

start = timer()
board: list[list[str]] = []


def is_symbol(s: str) -> bool:
    return not s.isdigit() and not s == "."


with open(data_file, encoding="utf-8") as f:
    for l in f.read().splitlines():
        board.append(list(l))

width = len(board[0])
height = len(board)

board_aux: list[list[bool]] = [[False for _ in range(width)] for _ in range(height)]

for i in range(height):
    for j in range(width):
        if board[i][j].isdigit():
            if (
                (not i == 0 and not j == 0 and is_symbol(board[i - 1][j - 1]))
                or (not i == 0 and is_symbol(board[i - 1][j]))
                or (
                    not i == 0 and not j == width - 1 and is_symbol(board[i - 1][j + 1])
                )
                or (not j == 0 and is_symbol(board[i][j - 1]))
                or (not j == width - 1 and is_symbol(board[i][j + 1]))
                or (
                    not i == height - 1
                    and not j == 0
                    and is_symbol(board[i + 1][j - 1])
                )
                or (not i == height - 1 and is_symbol(board[i + 1][j]))
                or (
                    not i == height - 1
                    and not j == width - 1
                    and is_symbol(board[i + 1][j + 1])
                )
            ):
                board_aux[i][j] = True


for i in range(height):
    for j in range(width):
        if board_aux[i][j]:
            end_left = False
            p = 0
            while not end_left and j - p != -1:
                if board[i][j - p].isdigit():
                    board_aux[i][j - p] = True
                    p += 1
                else:
                    end_left = True

            end_right = False
            p = 0
            while not end_right and j + p != width:
                if board[i][j + p].isdigit():
                    board_aux[i][j + p] = True
                    p += 1
                else:
                    end_right = True

for i in range(height):
    for j in range(width):
        if not board_aux[i][j]:
            board[i][j] = " "

result: list[int] = []
for l in board:
    string = "".join(l)
    numbers = re.findall(r"(\d+)", string)
    result.extend([int(number) for number in numbers])

print(f"Result: {sum(result)}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
