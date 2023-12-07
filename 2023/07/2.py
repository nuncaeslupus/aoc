from __future__ import annotations

from collections import Counter
from timeit import default_timer as timer

data_file = "sample.txt"
data_file = "data.txt"

result = None

FIVE = 6
FOUR = 5
HOUSE = 4
THREE = 3
TWO = 2
ONE = 1
HIGH = 0

strengths = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


class Hand:
    def __init__(self, hand: str, bid: int) -> None:
        self.hand = hand
        self.bid = bid
        self.rank = self.compute_rank()

    def compute_rank(self) -> int:
        counter = Counter(self.hand)
        counts = sorted(counter.values(), reverse=True)
        if counts[0] == 5:
            return FIVE
        if counts[0] == 4:
            if "J" in counter:
                return FIVE
            return FOUR
        if counts[0] == 3:
            if counts[1] == 2:
                if "J" in counter:
                    return FIVE
                return HOUSE
            if "J" in counter:
                return FOUR
            return THREE
        if counts[0] == 2:
            if counts[1] == 2:
                if counter.get("J", 0) == 2:
                    return FOUR
                if counter.get("J", 0) == 1:
                    return HOUSE
                return TWO
            if "J" in counter:
                return THREE
            return ONE
        if counts[0] == 1:
            if "J" in counter:
                return ONE
            return HIGH
        return HIGH

    def __gt__(self, other: Hand) -> bool:
        if self.rank > other.rank:
            return True
        if other.rank > self.rank:
            return False
        for i in range(len(self.hand)):
            if strengths[self.hand[i]] > strengths[other.hand[i]]:
                return True
            if strengths[other.hand[i]] > strengths[self.hand[i]]:
                return False
        return False

    def __repr__(self) -> str:
        return f"{self.hand} {self.rank} {self.bid}"


hands: list[Hand] = []

start = timer()
with open(data_file, encoding="utf-8") as f:
    for l in f.read().splitlines():
        hand, bid = tuple(l.split())
        hands.append(Hand(hand, int(bid)))

results = [hand.bid * (i + 1) for i, hand in enumerate(sorted(hands))]
result = sum(results)
print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
