rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)], 
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]

jets = [1 if x == '>' else -1 for x in open("/Users/julian/fun/AoC/2022/Day17/input.txt").read().strip()]

# ground is located at y = -1
solid = {(x, -1) for x in range(7)}

height = 0
rock_count = 0
rock_index = 0

# put the first rock in the correct position
rock = {(x + 2, height + y + 3) for x, y in rocks[rock_index]}

while rock_count < 2022:
    for jet in jets:
        # move rock to the left or right
        moved_rock = {(x + jet, y) for x, y in rock}
        # check if rock is still in the grid and if it intersects with solid rocks
        if all(x >= 0 and x < 7 for x, _ in moved_rock) and not len(solid.intersection(moved_rock)) > 0:
            rock = moved_rock
        # move rock down
        moved_rock = {(x, y - 1) for x, y in rock}
        # check if the rock intersects with solid rocks
        if len(solid.intersection(moved_rock)) > 0:
            # add rock to solid rocks
            solid.update(rock)
            rock_count += 1
            height = max(solid, key=lambda x: x[1])[1] + 1
            if rock_count >= 2022:
                break
            # put the next rock in the correct position
            rock_index = (rock_index + 1) % 5
            rock = {(x + 2, height + y + 3) for x, y in rocks[rock_index]}
        else:
            rock = moved_rock

print(f"Part one: {height}")

solid = {(x, -1) for x in range(7)}

seen = {}

def last_rows():
    o = [-100] * 7
    for x, y in solid:
        o[x] = max(o[x], y)
    top = max(o)
    return tuple(x - top for x in o)

height = 0
rock_count = 0
rock_index = 0

T = 1_000_000_000_000

# put the first rock in the correct position
rock = {(x + 2, height + y + 3) for x, y in rocks[rock_index]}

# Idea from YT: https://www.youtube.com/watch?v=w9Sk7lvyGZI
while rock_count < T:
    for jet_index, jet in enumerate(jets):
        # move rock to the left or right
        moved_rock = {(x + jet, y) for x, y in rock}
        # check if rock is still in the grid and if it intersects with solid rocks
        if all(x >= 0 and x < 7 for x, _ in moved_rock) and not len(solid.intersection(moved_rock)) > 0:
            rock = moved_rock
        # move rock down
        moved_rock = {(x, y - 1) for x, y in rock}
        # check if the rock intersects with solid rocks
        if len(solid.intersection(moved_rock)) > 0:
            # add rock to solid rocks
            solid.update(rock)
            rock_count += 1
            height = max(solid, key=lambda x: x[1])[1] + 1
            if rock_count >= T:
                break
            # put the next rock in the correct position
            rock_index = (rock_index + 1) % 5
            rock = {(x + 2, height + y + 3) for x, y in rocks[rock_index]}
            key = (jet_index, rock_index, last_rows())
            if key in seen:
                lrc, lh = seen[key]
                remainder = T - rock_count
                rep = remainder // (rock_count - lrc) 
                offset = rep * (height - lh)
                rock_count += rep * (rock_count - lrc)
                seen = {}
            seen[key] = (rock_count, height)
        else:
            rock = moved_rock

print(f"Part two: {height+offset}")
