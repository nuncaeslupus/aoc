from timeit import default_timer as timer
import re
import numpy as np
from typing import Optional

data_file = "sample.txt"
row_number = 10
data_file = "data.txt"
row_number = 2000000


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.distance: Optional[int] = None

    def manhattan_distance(self, other: "Coordinate"):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}). Dist to beacon: {self.distance}."


def find_not_accessible_in_row(
    sensor: Coordinate,
    row_number: int,
    beacons_x: list[int],
    row: list[bool],
    ini_x: int,
    end_x: int,
) -> None:

    min_x = sensor.x - (sensor.distance - abs(row_number - sensor.y))
    max_x = sensor.x * 2 - min_x
    for i in range(min_x, max_x + 1):
        if i not in beacons_x:
            row[i - ini_x] = row[i - ini_x] and False


start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()

    sensors: list[Coordinate] = []
    beacons: list[Coordinate] = []
    ini = Coordinate(np.inf, np.inf)
    end = Coordinate(-np.inf, -np.inf)
    row: list[int]

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

        ini.x = min([ini.x, sensor.x - sensor.distance])
        ini.y = min([ini.y, sensor.y - sensor.distance])
        end.x = max([end.x, sensor.x + sensor.distance])
        end.y = max([end.y, sensor.y + sensor.distance])

    row_impossible = [True] * (end.x - ini.x + 1)
    beacons_in_row = [beacon.x for beacon in beacons if beacon.y == row_number]
    for i, sensor in enumerate(sensors):
        find_not_accessible_in_row(
            sensor, row_number, beacons_in_row, row_impossible, ini.x, end.x
        )

    result = np.count_nonzero(np.invert(row_impossible))
    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
