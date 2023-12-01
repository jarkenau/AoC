import re

not_position = set()
beacons = set()

Y = 2_000_000

for line in open("input.txt"):
    sx, sy, bx, by = map(int, re.findall(r"(\d+)", line))
    distance = abs(sx - bx) + abs(sy - by)
    offset = distance - abs(sy - Y)
    if offset < 0:
        continue
    for x in range(sx - offset, sx + offset + 1):
        not_position.add(x)
    if by == Y:
        beacons.add(bx)

print(len(not_position - beacons))