from timeit import default_timer as timer
import re
import numpy as np
from typing import Optional
from collections import defaultdict

data_file = "sample.txt"
max_number = 20
data_file = "data.txt"
max_number = 4000000


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.distance: Optional[int] = None

    def manhattan_distance(self, other: "Coordinate"):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}). Dist to beacon: {self.distance}."


def find_empty_position(sensors: list[Coordinate], num_rows: int):
    for i in range(num_rows):
        row = []
        for sensor in sensors:
            row_difference = abs(i - sensor.y)
            if row_difference < sensor.distance:
                min_x = sensor.x - (sensor.distance - row_difference)
                max_x = sensor.x * 2 - min_x
                row.append((max(min_x, 0), min(max_x, num_rows)))
        position = find_row_empty_position(sorted(row), num_rows)
        if position is not None:
            return (position, i)
    return None


def find_row_empty_position(row: list, num_cols: int):
    min_value = num_cols
    max_value = 0
    for ini, end in row:
        if ini > max_value:
            return max_value + 1
        min_value = min(min_value, ini)
        max_value = max(max_value, end)
    return None


start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()

    sensors: list[Coordinate] = []
    beacons: list[Coordinate] = []
    ini = Coordinate(np.inf, np.inf)
    end = Coordinate(-np.inf, -np.inf)
    row: list[int]
    frequency = 4000000

    result = None
    for l in lines:
        data = re.search(
            "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
            l,
        )
        sensor = Coordinate(int(data.group(1)), int(data.group(2)))
        beacon = Coordinate(int(data.group(3)), int(data.group(4)))
        sensors.append(sensor)
        beacons.append(beacon)

    for i, sensor in enumerate(sensors):
        sensor.distance = sensor.manhattan_distance(beacons[i])

    rows_intervals = defaultdict(list)
    position = find_empty_position(sensors, max_number + 1)

    result = position[0] * frequency + position[1]
    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
