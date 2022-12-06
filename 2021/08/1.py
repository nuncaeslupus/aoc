data_file = "sample.txt"
data_file = "data.txt"

lengths = [2, 3, 4, 7]
with open(data_file) as f:
    lines = f.read().splitlines()

    counts = 0
    for l in lines:
        _, digits = l.split(" | ")
        numbers = digits.split()
        for n in numbers:
            if len(n) in lengths:
                counts += 1
    print(counts)
