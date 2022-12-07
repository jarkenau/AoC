stacks, moves = [crate.split("\n") for crate in open("input.txt").read().split("\n\n")]

def parse(stacks:str) -> list:
    stack = [[] for _ in range(10)]
    for line in stacks[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ":
                stack[i].insert(0, box) # requires shifting of the hole list
    return stack

stacksMatrix = parse(stacks)

for move in moves[:-1]:
    _, number, _ , src , _ , dst = move.split()
    for _ in range(int(number)):
        crate = stacksMatrix[int(src) - 1].pop()
        stacksMatrix[int(dst) - 1].append(crate)

top = ""
for stack in stacksMatrix:
    if stack:
        top += stack[-1]

assert(top == "LJSVLTWQM")
print(f"Part one: {top}")

stacksMatrix = parse(stacks)

for move in moves[:-1]:
    _, number, _ , src , _ , dst = move.split()
    crates = []
    for _ in range(int(number)):
        crates.append(stacksMatrix[int(src) - 1].pop())
    stacksMatrix[int(dst) -1].extend(reversed(crates))

top = ""
for stack in stacksMatrix:
    if stack:
        top += stack[-1]

assert(top == "BRQWDBBJM")
print(f"Part two {top}")

