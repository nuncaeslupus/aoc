with open("data.txt") as f:
    max = 0
    sum = 0
    for l in f.readlines():
        if l != "\n":
            sum += int(l)
        else:
            if sum > max:
                max = sum
            sum = 0
    print(max)
