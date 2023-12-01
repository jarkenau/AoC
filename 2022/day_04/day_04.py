pairs =[[int(section) for section in sections.replace("-", ",").split(",")] for sections in open("input.txt").read().strip().split("\n")]

def fullyContains(l1:int, l2:int, r1:int, r2:int) -> bool:
    return (l1 >= r1 and l2 <= r2) or (r1 >= l1 and r2 <= l2)

def contains(l1:int, l2:int, r1:int, r2:int) -> bool:
    return len((set(range(l1, l2 + 1)).intersection(set(range(r1, r2 + 1))))) >= 1

score = sum([fullyContains(l1, l2, r1, r2) for l1, l2, r1, r2 in pairs])

assert(score == 528)
print(f"First score {score}")

score = sum( [contains(l1, l2, r1, r2) for l1, l2, r1, r2 in pairs])

assert(score == 881)
print(f"Second score {score}")