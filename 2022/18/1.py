from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"


def touching(a: tuple[int, int, int], b: tuple[int, int, int]) -> bool:
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) == 1


start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()

    result = None
    free_sides = [6 for _ in range(len(lines))]
    coordinates: list[tuple[int, int, int]] = []

    for l in lines:
        x, y, z = l.split(",")
        coordinates.append((int(x), int(y), int(z)))

    for i in range(len(coordinates)):
        for j in range(i, len(coordinates)):
            if touching(coordinates[i], coordinates[j]):
                free_sides[i] -= 1
                free_sides[j] -= 1

    result = sum(free_sides)

    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
