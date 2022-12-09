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

all_scores = {")": 1, "]": 2, "}": 3, ">": 4}


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
    scores = []

    for l in lines:
        current_tree: Optional[Tree] = None

        completion = ""
        corrupted = False
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
                    corrupted = True
                    break
                else:
                    current_tree.closing = c
                    current_tree = current_tree.parent

        if not corrupted and not current_tree.closed:
            completion += open_close[current_tree.opening]
            parent = current_tree.parent
            while parent:
                current_tree = parent
                parent = current_tree.parent
                completion += open_close[current_tree.opening]

            line_score = 0
            for c in completion:
                line_score *= 5
                line_score += all_scores[c]
            scores.append(line_score)
    scores = sorted(scores)
    result = scores[len(scores) // 2]
    print(result)

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
