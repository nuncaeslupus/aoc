from timeit import default_timer as timer
from typing import Any, Optional
import json

data_file = "sample.txt"
data_file = "data.txt"


class Tree:
    def __init__(
        self, name: str, type: str, size: int, parent: Optional["Tree"]
    ) -> None:
        self.name = name
        self.type = type  # ["d", "f"]
        self.size = size
        self.parent = parent
        self.subtrees = []

    def add_subtree(self, subtree: "Tree") -> None:
        if not subtree.parent:
            subtree.parent = self
        self.subtrees.append(subtree)

    def subtree(self, name: str) -> "Tree":
        for st in self.subtrees:
            if st.name == name:
                return st
        return None

    def __str__(self) -> str:
        return (
            f"Tree {self.name}:\n"
            f"  {self.type}\n"
            f"  {self.size}\n"
            f"  {self.parent.name if self.parent else 'No parent'}\n"
            f"  {self.subtrees}\n"
        )

    def compute_size(self) -> None:
        size = 0
        for st in self.subtrees:
            if st.type == "f":
                size += st.size
            else:
                st.compute_size()
                size += st.size
        self.size = size

    def get_sizes(self, sizes: list[int]) -> None:
        sizes.append(self.size)
        for st in self.subtrees:
            if st.type == "d":
                st.get_sizes(sizes)


start = timer()
with open(data_file) as f:
    lines = f.read().splitlines()

    result = None
    tree: Optional[Tree] = None
    current_tree: Optional[Tree] = None
    for l in lines:
        parts = l.split()
        if parts[0] == "$":  # Command
            if parts[1] == "cd":  # Navigate
                if parts[2] == "/":
                    if not tree:
                        tree = Tree(parts[2], "d", 0, None)
                        current_tree = tree
                elif parts[2] == "..":
                    current_tree = current_tree.parent
                else:  # Into dir
                    subtree = current_tree.subtree(parts[2])
                    if not subtree:
                        subtree = Tree(parts[2], "d", 0, current_tree)
                        current_tree.add_subtree(subtree)
                    current_tree = subtree

            else:  # ls
                pass
        else:  # ls result
            if parts[0] == "dir":
                if not current_tree.subtree(parts[1]):
                    subtree = Tree(parts[1], "d", 0, current_tree)
                    current_tree.add_subtree(subtree)
            else:  # File
                if not current_tree.subtree(parts[1]):
                    subtree = Tree(parts[1], "f", int(parts[0]), current_tree)
                    current_tree.add_subtree(subtree)

    tree.compute_size()
    sizes = []
    tree.get_sizes(sizes)
    sizes = sorted(sizes)

    total_space = 70000000
    needed_space = 30000000
    current_space = total_space - tree.size
    needed_delete = needed_space - current_space
    for size in sizes:
        if size >= needed_delete:
            result = size
            break

    print(f"Result: {result}")


end = timer()
print(f"Total time: {end - start:.5f} seconds.")
