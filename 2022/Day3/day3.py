FILENAME = "input.txt"

def convertToNumber(string:str) -> int:
    if string.isupper():
        return ord(string) - 38
    else:
        return ord(string) - 96

items = [[item[:len(item)//2], item[len(item)//2:]] for item in open(FILENAME).read().strip().split("\n")]

score = 0
for firstHalf, secondHalf in items:
    commonChar = "".join(set(firstHalf).intersection(secondHalf))
    score += convertToNumber(commonChar)

assert(score == 7763) 
print(f"First score {score}")

score = 0
items = [item for item in open(FILENAME).read().strip().split("\n")]

for i in range(0, len(items), 3):
    sets = [set(i) for i in items[i:i+3]]
    commonChar = "".join(set.intersection(*sets))
    score += convertToNumber(commonChar)

assert(score == 2569)
print(f"Second score: {score}")

    