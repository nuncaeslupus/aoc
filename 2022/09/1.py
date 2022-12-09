from timeit import default_timer as timer
import numpy as np

data_file = "sample.txt"
data_file = "data.txt"


def compute_position(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    # Distance: sign, value
    dx = (np.sign(head[0] - tail[0]), abs(head[0] - tail[0]))
    dy = (np.sign(head[1] - tail[1]), abs(head[1] - tail[1]))
    if dx[1] == dy[1] and dx[1] == 2:
        tail = (tail[0] + dx[0], tail[1])
        tail = (tail[0], tail[1] + dy[0])
    elif dx[1] > dy[1] and dx[1] > 1 or dy[1] > dx[1] and dy[1] > 1:
        tail = (tail[0] + dx[0], tail[1])
        tail = (tail[0], tail[1] + dy[0])
    elif dx[1] == 0 and dy[1] > 1:
        tail = (tail[0], tail[1] + dy[0] * dy[1])
    elif dy[1] == 0 and dx[1] > 1:
        tail = (tail[0] + dx[0] * dx[1], tail[1])

    return tail


start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()
    visited: set[tuple[int, int]] = {(0, 0)}
    head = (0, 0)
    tail = (0, 0)
    for l in lines:
        parts = l.split()
        direction = parts[0]
        amount = int(parts[1])

        for i in range(amount):
            if direction == "U":
                head = (head[0], head[1] + 1)
            elif direction == "D":
                head = (head[0], head[1] - 1)
            elif direction == "R":
                head = (head[0] + 1, head[1])
            else:
                head = (head[0] - 1, head[1])

            tail = compute_position(head, tail)
            visited.add(tail)

    result = len(visited)
    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
