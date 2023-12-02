from math import prod
from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

cube_order = {"red": 0, "green": 1, "blue": 2}

start = timer()
with open(data_file, encoding="utf-8") as f:
    min_cubes: list[list[int]] = []
    result: list[int] = []
    for l in f:
        current_game_min = [0, 0, 0]
        game_num, games = l.split(":")
        game_num = game_num.split()[1]
        for game in games.split(";"):
            for cubes in game.split(","):
                num_cubes, color = cubes.split()
                current_game_min[cube_order[color]] = max(
                    current_game_min[cube_order[color]], int(num_cubes)
                )
        result.append(prod(current_game_min))

    print(f"Result: {sum(result)}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
