from collections import deque
import re

data_file = "sample.txt"
data_file = "data.txt"

with open(data_file) as f:
    lines = f.read().splitlines()
    line_length = len(lines[0])
    num_stacks = (line_length + 1) // 4
    stacks = [deque() for i in range(num_stacks)]

    crates = True
    for l in lines:
        if crates:
            if l[1].isdigit():
                crates = False
            else:
                for i in range(0, line_length, 4):
                    if l[i] == "[":
                        stacks[i // 4].appendleft(l[i + 1])
        else:
            move_match = re.search("move (\d*) from (\d*) to (\d*)", l)
            if move_match:
                num_moves = int(move_match.group(1))
                move_from = int(move_match.group(2))
                move_to = int(move_match.group(3))

                for move in range(num_moves):
                    stacks[move_to - 1].append(stacks[move_from - 1].pop())
    print("".join([stack.pop() for stack in stacks]))
