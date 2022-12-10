from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"


def render_image(screen: list) -> None:
    for row in screen:
        print("".join(row))


start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()

    screen_width = 40
    screen_height = 6

    time = 0
    reg = 1
    crt_x = 0
    crt_y = 0
    screen = [["." for _ in range(screen_width)] for _ in range(screen_height)]

    for l in lines:
        crt_x = time % 40
        crt_y = time // 40

        if crt_x in range(reg - 1, reg + 2):
            screen[crt_y][crt_x] = "#"
        time += 1

        if l != "noop":
            crt_x = time % 40
            crt_y = time // 40
            amount = int(l.split()[1])
            if crt_x in range(reg - 1, reg + 2):
                screen[crt_y][crt_x] = "#"
            time += 1
            reg += amount

    render_image(screen)

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
