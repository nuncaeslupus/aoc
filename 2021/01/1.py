datafile = "data.txt"

with open(datafile) as f:
    lines = f.read().splitlines()

    previous_value = int(lines[0])
    count = 0
    for l in lines:
        current_value = int(l)
        if current_value > previous_value:
            count += 1
        previous_value = current_value
    print(count)
