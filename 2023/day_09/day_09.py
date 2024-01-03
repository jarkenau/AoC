from functools import reduce

readings = [list(map(int, line.split())) for line in open("input.txt").readlines()]

next_vals_part_one = []
next_vals_part_two = []

for reading in readings:
    front_values, back_values = [reading[0]], [reading[-1]]
    current = reading
    while not all(val == 0 for val in current):
        diff = [second - first for first, second in zip(current[:-1], current[1:])]
        back_values.append(diff[-1])
        front_values.append(diff[0])
        current = diff
    next_vals_part_two.append(reduce(lambda x, y: y - x, front_values[::-1]))
    next_vals_part_one.append(sum(back_values))

part_one = sum(next_vals_part_one)
part_two = sum(next_vals_part_two)

print(f"Part one: {part_one}")
print(f"Part two: {part_two}")
