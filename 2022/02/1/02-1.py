score = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

with open("data.txt") as f:
    total = 0
    for l in f.readlines():
        print(l[:3])
        total += score[l[:3]]
    print(total)
