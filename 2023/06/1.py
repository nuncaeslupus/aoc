from math import ceil, prod
from timeit import default_timer as timer


data_file = "sample.txt"
data_file = "data.txt"

races: list[tuple[int, int]] = []
results: list[int] = []
start = timer()
with open(data_file, encoding="utf-8") as f:
    result = None
    lines = f.read().splitlines()
    times = lines[0].split(":")[1].split()
    distances = lines[1].split(":")[1].split()
    races = [(int(pair[0]), int(pair[1])) for pair in zip(times, distances)]

for race in races:
    count = 0
    for i in range(ceil(race[0] / 2)):
        if (race[0] - i) * i > race[1]:
            count += 2
    if race[0] % 2 == 0:
        count += 1
    results.append(count)

print(f"Result: {prod(results)}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
