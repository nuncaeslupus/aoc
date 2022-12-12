from timeit import default_timer as timer
from collections import deque
from math import prod
from typing import Callable

data_file = "sample.txt"
data_file = "data.txt"


class Monkey:
    def __init__(
        self,
        starting_items: deque[int],
        operation: tuple[Callable, int],
        test_div: tuple[int, int, int],
    ) -> None:
        self.items = starting_items
        self.operation = operation
        self.test_div = test_div
        self.inspections = 0

    def inspect(self, monkeys: "list[Monkey]"):
        while len(self.items):
            item = self.items.popleft()
            if self.operation[0] in [sum, prod]:
                item = self.operation[0]([item, self.operation[1]])
            else:
                item *= item
            item = round(item // 3)
            div = item % self.test_div[0]
            if not div:
                monkeys[self.test_div[1]].add_item(item)
            else:
                monkeys[self.test_div[2]].add_item(item)
            self.inspections += 1

    def add_item(self, item: int):
        self.items.append(item)

    def __str__(self) -> str:
        string = f" Items: {self.items}\n Operation: {self.operation}\n"
        string += f" Test div: {self.test_div}\n Total inspections: {self.inspections}"
        return string


def print_monkeys(monkeys: list[Monkey]) -> None:
    for i, monkey in enumerate(monkeys):
        print(f"Monkey {i}:")
        print(monkey)


start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()
    rounds = 20

    monkeys: list[Monkey] = []
    inspections: list[int] = []
    result = None

    for l in range(0, len(lines), 7):
        its = lines[l + 1].replace(",", "").split()[2:]
        items = deque([int(item) for item in its])
        op = lines[l + 2].split()[-2:]
        if op[0] == "+":
            if op[1] != "old":
                operation = (sum, int(op[1]))
            else:
                operation = (prod, 2)
        elif op[0] == "*":
            if op[1] != "old":
                operation = (prod, int(op[1]))
            else:
                operation = (pow, 2)
        tst = int(lines[l + 3].split()[-1])
        tr = int(lines[l + 4].split()[-1])
        fs = int(lines[l + 5].split()[-1])
        test = (tst, tr, fs)
        monkey = Monkey(items, operation, test)
        monkeys.append(monkey)

    for i in range(rounds):
        for monkey in monkeys:
            monkey.inspect(monkeys)

    inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)

    result = prod(inspections[:2])

    print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
