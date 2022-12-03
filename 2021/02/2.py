datafile = "data.txt"

with open(datafile) as f:
    lines = f.read().splitlines()

    hor = 0
    depth = 0
    aim = 0
    for l in lines:
        direction, amount = l.split()
        if direction == "forward":
            hor += int(amount)
            depth += aim * int(amount)
        elif direction == "up":
            aim -= int(amount)
        elif direction == "down":
            aim += int(amount)
    print(f"{hor} x {depth} = {hor * depth}")
