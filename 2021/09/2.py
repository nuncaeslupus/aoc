from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()

    table = []
    for i, l in enumerate(lines):
        row = [int(c) for c in l]
        table.append(row)

    pairs = set()
    height, width = len(table), len(table[0])

    # Generate grups of pairs of connected positions
    groups: "list[set(int)]" = []
    for i in range(height):
        for j in range(width):
            if table[i][j] != 9:
                pairs = []
                if i != height - 1 and table[i + 1][j] != 9:
                    pairs.append(tuple(sorted([i * width + j, (i + 1) * width + j])))
                if j != width - 1 and table[i][j + 1] != 9:
                    pairs.append(tuple(sorted([i * width + j, i * width + j + 1])))
                if pairs:
                    for pair in pairs:
                        for group in groups:
                            if pair[0] in group:
                                group.add(pair[1])
                                break
                            elif pair[1] in group:
                                group.add(pair[0])
                                break
                        else:
                            new_group = set([pair[0], pair[1]])
                            groups.append(new_group)

    # Join groups
    new_groups: "list[set(int)]" = []
    for group in groups:
        for i, new_group in enumerate(new_groups):
            if group.intersection(new_group):
                new_groups[i] = new_group.union(group)
                break
        else:
            new_groups.append(group)

    new_groups = sorted(new_groups, key=len, reverse=True)
    total_size = len(new_groups[0]) * len(new_groups[1]) * len(new_groups[2])
print(f"Result: {total_size}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
