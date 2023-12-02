from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

max_cubes = {"red": 12, "green": 13, "blue": 14}

start = timer()
with open(data_file, encoding="utf-8") as f:
    possible_games: list[int] = []
    result = None
    for l in f:
        possible = True
        game_num, games = l.split(":")
        game_num = game_num.split()[1]
        for game in games.split(";"):
            for cubes in game.split(","):
                num_cubes, color = cubes.split()
                if max_cubes[color] < int(num_cubes):
                    possible = False
                    continue
            if not possible:
                continue
        if not possible:
            continue
        possible_games.append(int(game_num))

    print(f"Result: {sum(possible_games)}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
