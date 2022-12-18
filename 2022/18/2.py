from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"


def touching(a: tuple[int, int, int], b: tuple[int, int, int]) -> bool:
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) == 1


def find_pockets(
    water: set[tuple[int, int, int]], lava: set[tuple[int, int, int]]
) -> set[tuple[int, int, int]]:
    possible_pockets: set[tuple[int, int, int]] = set()
    for w in water:
        x_up, x_down = False, False
        y_up, y_down = False, False
        z_up, z_down = False, False
        for l in lava:
            if w[0] == l[0] and w[1] == l[1]:
                if w[2] < l[2]:
                    z_up = True
                else:
                    z_down = True
            elif w[0] == l[0] and w[2] == l[2]:
                if w[1] < l[1]:
                    y_up = True
                else:
                    y_down = True
            elif w[1] == l[1] and w[2] == l[2]:
                if w[0] < l[0]:
                    x_up = True
                else:
                    x_down = True
        if x_up and x_down and y_up and y_down and z_up and z_down:
            possible_pockets.add(w)

    only_water = list(water.difference(possible_pockets))
    all_found = False

    while not all_found:
        possible_pockets_list = list(possible_pockets)
        new_water = []
        for i in range(len(possible_pockets_list)):
            for j in range(len(only_water)):
                if touching(possible_pockets_list[i], only_water[j]):
                    new_water.append(possible_pockets_list[i])
        if len(new_water) == 0:
            all_found = True
        else:
            possible_pockets = possible_pockets.difference(new_water)
            only_water = new_water.copy()

    return possible_pockets


start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()
    result = None

    min_x, min_y, min_z = 10000, 10000, 10000
    max_x, max_y, max_z = -10000, -10000, -10000

    lava: set[tuple[int, int, int]] = set()
    water: set[tuple[int, int, int]] = set()
    for l in lines:
        x, y, z = l.split(",")
        new_coord = (int(x), int(y), int(z))
        min_x = min(min_x, new_coord[0])
        min_y = min(min_y, new_coord[1])
        min_z = min(min_z, new_coord[2])
        max_x = max(max_x, new_coord[0])
        max_y = max(max_y, new_coord[1])
        max_z = max(max_z, new_coord[2])

        lava.add(new_coord)

    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                water.add((x, y, z))

    water = water.difference(lava)
    in_pockets = find_pockets(water, lava)
    not_water = list(in_pockets.union(lava))

    free_sides = [6 for _ in range(len(not_water))]

    for i in range(len(not_water)):
        for j in range(i, len(not_water)):
            if touching(not_water[i], not_water[j]):
                free_sides[i] -= 1
                free_sides[j] -= 1

    result = sum(free_sides)

    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
