from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()

    time = 1
    reg = 1
    result = 0

    for l in lines:
        if l == "noop":
            time += 1
        else:
            amount = int(l.split()[1])
            time += 2
            if (time - 20) % 40 == 1:
                result += (time - 1) * reg

            reg += amount
        if (time - 20) % 40 == 0:
            result += time * reg

    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
