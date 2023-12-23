times, distances = [list(map(int, line.split(":")[1].split())) for line in open("2023/day_06/input.txt").readlines()]

total_ways = 1
for time, distance in zip(times, distances):
    num_ways = 0
    for speed in range(1, time):
        if (time - speed) * speed > distance:
            num_ways += 1
    total_ways *= num_ways

print(f"Part one {total_ways}")

time =  int("".join([str(i) for i in times]))
distance = int("".join([str(i) for i in distances]))

# TODO: work on a more efficient solution
num_ways = 0 
for speed in range(1, time):
    travel_distance = (time - speed) * speed
    if travel_distance > distance:
        num_ways += 1

print(f"Part two: {num_ways}")        