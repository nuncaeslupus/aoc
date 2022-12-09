from timeit import default_timer as timer
from typing import Optional

data_file = "sample.txt"
data_file = "data.txt"

open_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

all_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


class Tree:
    def __init__(self, opening: str, parent: Optional["Tree"] = None) -> None:
        self.opening = opening
        self.closing = open_close[opening]
        self.subtrees: list["Tree"] = []
        self.parent = parent
        self.closed = False

    def add_subtree(self, subtree: "Tree") -> None:
        self.subtrees.append(subtree)


start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()

    result = 0
    corrupted_chars = ""

    for l in lines:
        current_tree: Optional[Tree] = None
        for c in l:

            if c in open_close.keys():
                if not current_tree:
                    t = Tree(c)
                else:
                    t = Tree(c, current_tree)
                    current_tree.add_subtree(t)
                current_tree = t
            else:
                if c != open_close[current_tree.opening]:  # Corrupted
                    corrupted_chars += c
                    result += all_scores[c]
                    break
                else:
                    current_tree.closing = c
                    current_tree = current_tree.parent

    print(result)

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
