from timeit import default_timer as timer
import numpy as np

data_file = "sample.txt"
data_file = "data.txt"

start = timer()
result = None
with open(data_file) as f:

    lines = f.read().splitlines()
    numbers = np.array(lines, dtype=np.int32)
    positions = np.array(range(len(numbers)))
    num_pos = np.row_stack((numbers, positions))

    length = len(positions)
    for i in range(len(numbers)):
        old_position = np.where(num_pos[1] == i)[0][0]
        element = num_pos[0][old_position]

        item = num_pos[:, old_position]
        num_pos = np.hstack(
            (
                num_pos[:, :old_position].reshape((2, -1)),
                num_pos[:, old_position + 1 :].reshape((2, -1)),
            )
        )

        lower = old_position + item[0] <= 0
        upper = old_position + item[0] >= length
        num_pos = np.roll(num_pos, -item[0] - old_position, axis=1)
        num_pos = np.hstack((item.reshape(2, -1), num_pos))
        num_pos = np.roll(
            num_pos, item[0] + old_position - int(lower) + int(upper), axis=1
        )

    pos_0 = np.where(num_pos[0] == 0)[0][0]
    pos_1000 = num_pos[0][(pos_0 + 1000) % length]
    pos_2000 = num_pos[0][(pos_0 + 2000) % length]
    pos_3000 = num_pos[0][(pos_0 + 3000) % length]
    result = pos_1000 + pos_2000 + pos_3000
    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
