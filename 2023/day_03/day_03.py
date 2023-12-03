from typing import List

lines = [[char for char in line] for line in open("input.txt").read().strip().split("\n")]

def get_numbers(start_cords: set) -> List[int]:
    """Extract the numbers based on their start coordinate"""
    numbers = []
    for r, c in start_cords:
        num = ""
        while c < len(lines[r]) and lines[r][c].isdigit():
            num += lines[r][c]
            c += 1
        numbers.append(int(num))
    return numbers

# set to store the starts of the numbers
part_one = set()
for r, row in enumerate(lines):
    for c, column in enumerate(row):
        if not column.isdigit() and not column == ".":
            # check area around a symbol
            for i in range(-1, 2):
                for j in range(-1, 2):
                    cr, cc = r+i, c+j 
                    # check if the area contains any number
                    if cr >= 0 and cr < len(lines) and cc >= 0 and cc < len(lines[cr]) and lines[cr][cc].isdigit():
                        # find the beginning of a number
                        while cc > 0 and lines[cr][cc-1].isdigit():
                            cc -= 1
                        part_one.add((cr, cc))

part_two = 0
for r, row in enumerate(lines):
    for c, column in enumerate(row):
        # only consider the area around '*' symbols
        if column == "*":
            neighbors = set()
            for i in range(-1, 2):
                for j in range(-1, 2):
                    cr, cc = r+i, c+j
                    if cr >= 0 and cr < len(lines) and cc >= 0 and cc < len(lines[cr]) and lines[cr][cc].isdigit():
                        # find the beginning of a number
                        while cc > 0 and lines[cr][cc-1].isdigit():
                            cc -= 1
                        neighbors.add((cr, cc))
            if len(neighbors) == 2:
                numbers = get_numbers(neighbors)
                part_two += numbers[0] * numbers [1]

print(f"Part one {sum(get_numbers(part_one))}")
print(f"Part two {part_two}")
    