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
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
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
            return FOUR
        if counts[0] == 3:
            if counts[1] == 2:
                return HOUSE
            return THREE
        if counts[0] == 2:
            if counts[1] == 2:
                return TWO
            return ONE
        return HIGH

    def __gt__(self, other: Hand) -> bool:
        self_rank = self.compute_rank()
        other_rank = other.compute_rank()

        if self_rank > other_rank:
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
        return f"{self.hand} {self.bid}"


hands: list[Hand] = []

start = timer()
with open(data_file, encoding="utf-8") as f:
    for l in f.read().splitlines():
        hand, bid = tuple(l.split())
        hands.append(Hand(hand, int(bid)))


result = sum([hand.bid * (i + 1) for i, hand in enumerate(sorted(hands))])

print(f"Result: {result}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
