lines = [line for line in open("input.txt").read().strip().split("\n")]

part_one = 0
for line in lines:
    nums = line.split(":")[1]
    a, b  = [list(map(int, k.split())) for k in nums.split(" | ")]
    intersect = set(a).intersection(set(b))
    if intersect:
        part_one += 2**(len(intersect) - 1)

m = {}
for card, line in enumerate(lines, 1):
    # count the initial cards
    if card not in m:
        m[card] = 1
    nums = line.split(":")[1]
    a, b  = [list(map(int, k.split())) for k in nums.split(" | ")]
    intersect = set(a).intersection(set(b))
    if intersect:
        # count the number of copy cards
        for win in range(card + 1, card + len(intersect) + 1):  
            m[win] = m.get(win, 1) + m[card]
            
print(f"Part one: {part_one}")
print(f"Part two: {sum(m.values())}")
