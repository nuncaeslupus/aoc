from timeit import default_timer as timer

data_file = "sample.txt"
# data_file = "data.txt"

start = timer()
with open(data_file, encoding="utf-8") as f:
    result = None
    for l in f:
        pass

    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
