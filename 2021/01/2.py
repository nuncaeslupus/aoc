datafile = "data.txt"

with open(datafile) as f:
    lines = f.read().splitlines()
    lines = [int(l) for l in lines]

    previous_value = lines[0] + lines[1] + lines[2]
    count = 0
    for i in range(len(lines) - 2):
        current_value = lines[i] + lines[i + 1] + lines[i + 2]
        if current_value > previous_value:
            count += 1
        previous_value = current_value
    print(count)
