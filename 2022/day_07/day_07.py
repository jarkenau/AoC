from collections import defaultdict
from itertools import accumulate

commands = [command.strip() for command in open("input.txt").read().strip().split("\n")]

sizes = defaultdict(int)
path = [] # keep track of the current path

# structural pattern matching (better switch case), python >= 3.10
# https://peps.python.org/pep-0636/#appendix-a-quick-intro
for command in commands:
    match command.split():
        case ["$", "cd", ".."]:
            path.pop()
        case ["$", "cd", dir]:
            path.append(dir)
        case ["$", "ls"]:
            pass
        case ["dir", _]:
            pass
        case [filesize, _ ]:
            # a list is not hashable, so we need to convert it to a tuple
            sizes[tuple(path)] += int(filesize)
            # propagate the size to the parent directories
            for i in range(len(path)):
                currPath = tuple(path[:i])
                if currPath:
                    sizes[currPath] += int(filesize)

firstCore = sum([size for size in sizes.values() if size < 100_000])

print("First core size:", firstCore)

freeSpace = 70_000_000 - sizes[("/", )] 

secondCore = min([size for size in sizes.values() if freeSpace + size >= 30_000_000])

print("Second core size:", secondCore)
