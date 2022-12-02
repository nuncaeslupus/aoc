score = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

with open("data.txt") as f:
    total = 0
    for l in f.readlines():
        print(l[:3])
        total += score[l[:3]]
    print(total)
