datafile = "data.txt"

with open(datafile) as f:
    lines = f.read().splitlines()

    hor = 0
    depth = 0
    for l in lines:
        direction, amount = l.split()
        if direction == "forward":
            hor += int(amount)
        elif direction == "up":
            depth -= int(amount)
        elif direction == "down":
            depth += int(amount)
    print(f"{hor} x {depth} = {hor * depth}")
