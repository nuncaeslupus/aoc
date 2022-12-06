from typing import Optional

data_file = "sample.txt"
data_file = "data.txt"


def decypher_patterns(
    patterns: "list[set[str]]", counts: "dict[str, int]"
) -> "dict[str, str]":
    """Occurrences: a: 8, b: 6, c: 8, d: 7, e: 4, f: 9, g: 7
    Patterns: 1, 7, 4, (2, 3, 5), (0, 6, 9), 8"""
    equivalences = {}
    for c, n in counts.items():
        if n == 6:
            equivalences["b"] = c
        elif n == 4:
            equivalences["e"] = c
        elif n == 9:
            equivalences["f"] = c
        elif n == 8:
            if c in patterns[0]:  # "1"
                equivalences["c"] = c
            else:
                equivalences["a"] = c
        else:
            if c in patterns[2]:  # "4"
                equivalences["d"] = c
            else:
                equivalences["g"] = c
    return equivalences


def create_fake_shapes(
    shapes: "dict[str, int]", equivalences: "dict[str, str]"
) -> "dict[str, int]":
    fake_shapes = {}
    for s, n in shapes.items():
        fake_s = ""
        for c in s:
            fake_s += equivalences[c]
        fake_shapes["".join(sorted(fake_s))] = n
    return fake_shapes


with open(data_file) as f:
    lines = f.read().splitlines()

    letters = ["a", "b", "c", "d", "e", "f", "g"]
    shapes = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    output = 0
    for l in lines:
        first, second = l.split(" | ")

        # Patterns (before " | ")
        all_letters = "".join(first.split())
        occurrences = [all_letters.count(l) for l in letters]
        counts = {l: c for l, c in zip(letters, occurrences)}
        patts = sorted(first.split(), key=len)
        patterns = [set(x) for x in patts]

        # Digits (after " | ")
        digits = ["".join(sorted(x)) for x in second.split()]

        # Find digits
        equivalences = decypher_patterns(patterns, counts)
        fake_shapes = create_fake_shapes(shapes, equivalences)

        number = 0
        for i, d in enumerate(digits):
            number += fake_shapes[d] * 10 ** (len(digits) - i - 1)
        output += number
    print(output)
