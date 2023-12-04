from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

start = timer()
table: list[tuple[set[int], set[int]]] = []
with open(data_file, encoding="utf-8") as f:
    result = None
    for l in f.read().splitlines():
        winning: set[int] = set()
        have: set[int] = set()
        groups = l.split("|")
        winning_list = groups[0].split(":")[1]
        winning = set([int(number) for number in winning_list.split()])
        have = set([int(number) for number in groups[1].split()])
        table.append((winning, have))

points: list[int] = []
for row in table:
    matches = len(row[0].intersection(row[1]))
    if matches:
        points.append(2 ** (matches - 1))
    else:
        points.append(0)

result = sum(points)
print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
