from timeit import default_timer as timer
from math import lcm

data_file = "sample3.txt"
data_file = "data.txt"

start = timer()
mapping: dict[str, tuple[str, str]] = {}
with open(data_file, encoding="utf-8") as f:
    result = None
    lines = f.read().splitlines()
    instructions = lines[0].replace("L", "0").replace("R", "1")
    for l in lines[2:]:
        l = l.replace("(", "").replace(")", "")
        key, ways = l.split(" = ")
        left, right = ways.split(", ")
        mapping[key] = (left, right)


result = 0
startings = [key for key in mapping.keys() if key[-1] == "A"]
ends = [key for key in mapping.keys() if key[-1] == "Z"]
startends = {key: {} for key in startings}

for starting in startings:
    pos = 0
    count = 1
    key = starting
    while key not in startends[starting]:
        key = mapping[key][int(instructions[pos])]
        pos = (pos + 1) % len(instructions)
        if key[-1] == "Z":
            startends[starting][key] = count
        count += 1

results = [[val for val in value.values()] for value in startends.values()]
result = lcm(*list(item[0] for item in results))
print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
