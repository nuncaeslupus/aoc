import re
from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

start = timer()
with open(data_file, "r") as f:

    result: list[int] = []
    for l in f:
        l = re.sub(r"\D", "", l)
        result.append(int(l[0]) * 10 + int(l[-1]))
    print(f"Result: {sum(result)}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
