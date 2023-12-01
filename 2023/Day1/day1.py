import re

lines = [line for line in open("input.txt").read().strip().split("\n")]

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def word_to_number(input: str) -> str:
    if input in numbers:
        return str(numbers.index(input) + 1)
    else:
        return input

part_one = 0
for line in lines:
    matches = re.findall(r'[0-9]', line)
    part_one += int(matches[0] + matches[-1])

part_two = 0
for line in lines:
    # full regex (?=([0-9]|one|two|three|four|five|six|seven|eight|nine))
    # use a non capturing group to match overlapping numbers like 'eightwothree'
    matches = re.findall("(?=([0-9]|" + "|".join(numbers) + "))", line)
    part_two += int(word_to_number(matches[0]) + word_to_number(matches[-1]))

print(f"Part one {part_one}")
print(f"Part two {part_two}")

        
