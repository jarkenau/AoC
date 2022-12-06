#!/usr/bin/env python3

# 1. read hole file and split on empty lines
# 2. iterate over list and remove the \n after each number
# 3. sum resulting list
calories = [sum([int(x) for x in b.split("\n")]) for b in open("input.txt").read().strip().split("\n\n")]

# cloud be done in one line, but this is more readable
part_one = max(calories)
part_two = sum(sorted(calories, reverse=True)[:3])

assert(part_two == 206152)
assert(part_one == 69528)

print(f"Part one: {part_one}")
print(f"Part two: {part_two}")