strategies = [[y for y in x if y != ' '] for x in open("input.txt").read().strip().split("\n")]

WIN = {"A": "Y", "B": "Z", "C": "X"}
DRAW = {"A": "X", "B": "Y", "C": "Z"}
LOSE  = {"A": "Z", "B": "X", "C": "Y"}
POINTS = {"X": 1, "Y": 2, "Z": 3}

score = 0
for opponent, me in strategies:
    score += POINTS[me]
    if me == WIN[opponent]:
        score += 6
    elif me == DRAW[opponent]:
        score += 3 

assert(score == 13675)
print(f"First score: {score}")

score = 0
for opponent, me in strategies:
    if me == "X":
        score += POINTS[LOSE[opponent]]
    elif me == "Y":
        score += POINTS[DRAW[opponent]] + 3
    else:
        score += POINTS[WIN[opponent]] + 6


assert(score==14184)
print(f"Second score: {score}")


