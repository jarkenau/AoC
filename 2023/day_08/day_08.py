import re

instructions, nodes = open("input.txt").read().split("\n\n")

network = {}
for node in nodes.strip().split("\n"):
    start, left, right = re.findall(r"[A-Z0-9]{3}", node)
    network[start] = {"L": left, "R": right}

current = "AAA"
steps = 0
while current != "ZZZ":
    steps += 1
    current = network[current][instructions[0]]
    instructions = instructions[1:] + instructions[0]

print(f"Part one: {steps}")

assert(steps == 20093)