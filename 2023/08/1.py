from timeit import default_timer as timer

data_file = "sample2.txt"
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
pos = 0
key = "AAA"
while key != "ZZZ":
    key = mapping[key][int(instructions[pos])]
    result += 1
    pos = (pos + 1) % len(instructions)


print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
