import copy

blocked_positions = set()
max_y = 0

for line in open('input.txt'):
    rock_positions = [list(map(int, pair.split(','))) for pair in line.strip().split(' -> ')]
    for i in range(len(rock_positions) - 1):
        x1, x2 = sorted([rock_positions[i][0], rock_positions[i+1][0]])
        y1, y2 = sorted([rock_positions[i][1], rock_positions[i+1][1]])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                blocked_positions.add((x, y))
                max_y = max(max_y, y + 1)

blocked_positions1 = copy.deepcopy(blocked_positions)

num_sand = 0
sand_below = False
while not sand_below:
    sand = (500, 0)
    while True:
        if sand[1] >= max_y:
            sand_below = True
            break
        # down
        if (sand[0], sand[1] + 1) not in blocked_positions:
            sand = (sand[0], sand[1] + 1)
            continue
        # down and left
        if (sand[0] - 1, sand[1] + 1) not in blocked_positions:
            sand = (sand[0] - 1, sand[1] + 1)
            continue
        # down and right
        if (sand[0] + 1, sand[1] + 1) not in blocked_positions:
            sand = (sand[0] + 1, sand[1] + 1)
            continue
        # sand can't fall any further
        blocked_positions.add(sand)
        num_sand += 1
        break

print(f"Part one: {num_sand}")

num_sand = 0
while (500, 0) not in blocked_positions1:
    sand = (500, 0)
    while True:
        # if the sand reaches the layer above the ground we stop it
        if sand[1] >= max_y:
            break
        # down
        if (sand[0], sand[1] + 1) not in blocked_positions1:
            sand = (sand[0], sand[1] + 1)
            continue
        # down and left
        if (sand[0] - 1, sand[1] + 1) not in blocked_positions1:
            sand = (sand[0] - 1, sand[1] + 1)
            continue
        # down and right
        if (sand[0] + 1, sand[1] + 1) not in blocked_positions1:
            sand = (sand[0] + 1, sand[1] + 1)
            continue
        break
    # sand can't fall any further
    blocked_positions1.add(sand)
    num_sand += 1

print(f"Part two: {num_sand}")