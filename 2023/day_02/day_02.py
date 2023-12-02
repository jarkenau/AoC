lines = [line for line in open("input.txt").read().strip().split("\n")]

part_one = 0
for game_id, line in enumerate(lines):
    games = line.strip().split(": ")[1].split("; ")
    possible = True
    for game in games:   
        cubes = {"red": 0, "blue": 0, "green": 0}
        for pair in game.split(", "):
            num_cubes, color = pair.split()
            cubes[color] = int(num_cubes)
        if cubes["red"] > 12 or cubes["green"] > 13 or cubes["blue"] > 14:
            possible = False
            break
    if possible:
        part_one += game_id + 1

part_two = 0
for line in lines:
    games = line.strip().split(": ")[1].split("; ")
    cubes = {"red": 0, "blue": 0, "green": 0}
    for game in games:
        for pair in game.split(", "):
            num_cubes, color = pair.split()
            cubes[color] = max(cubes[color], int(num_cubes))
    part_two += cubes["red"] * cubes["green"] * cubes["blue"]

print(f"Part one {part_one}")
print(f"Part two {part_two}")