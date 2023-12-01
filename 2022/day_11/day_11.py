from math import floor
from typing import List, Dict
import numpy as np
import copy

# use chinese remainder theorem to keep the numbers small
divisors = [11, 19, 5, 2, 13, 7, 3, 17]
prod = np.prod(divisors)


class Monkey:
    def __init__(self,
                 name: int,
                 items: List[int],
                 worry_increase: int,
                 worry_operation: str,
                 divisor: int,
                 passIfTrue: int,
                 passIfFalse: int):
        self.name = name
        self.items = items
        self.worry_increase = worry_increase
        self.worry_operation = worry_operation
        self.divisor = divisor
        self.passIfTrue = passIfTrue
        self.passIfFalse = passIfFalse
        self.inspected = 0

    def __str__(self) -> str:
        return f"Monkey {self.name} has {self.items}"

    def passItemPartOne(self, item: int, allMonkeys: Dict) -> None:
        worry_level = None
        if self.worry_operation == "+":
            worry_level = floor((item + self.worry_increase) / 3)
        elif self.worry_operation == "*":
            worry_level = floor((item * self.worry_increase) / 3)
        elif self.worry_operation == "**":
            worry_level = floor((item**2) / 3)
        if worry_level is not None:
            if worry_level % self.divisor == 0:
                allMonkeys[self.passIfTrue].items.append(worry_level)
            else:
                allMonkeys[self.passIfFalse].items.append(worry_level)

    def passItemPartTwo(self, item: int, allMonkeys: Dict) -> None:
        worry_level = None
        if self.worry_operation == "+":
            worry_level = item + self.worry_increase % prod
        elif self.worry_operation == "*":
            worry_level = item * self.worry_increase % prod
        elif self.worry_operation == "**":
            worry_level = item**2 % prod
        if worry_level is not None:
            if worry_level % self.divisor == 0:
                allMonkeys[self.passIfTrue].items.append(worry_level)
            else:
                allMonkeys[self.passIfFalse].items.append(worry_level)

    def passItems(self, part: int, allMonkeys: Dict) -> None:
        while len(self.items) > 0:
            if part == 1:
                self.passItemPartOne(self.items.pop(0), allMonkeys)
            elif part == 2:
                self.passItemPartTwo(self.items.pop(0), allMonkeys)
            self.inspected += 1


# generate objects manually, parsing the input seems tedious
monkeyDict = {}
monkeyDict[0] = Monkey(0, [97, 81, 57, 57, 91, 61], 7, "*", 11, 5, 6)
monkeyDict[1] = Monkey(1, [88, 62, 68, 90], 17, "*", 19, 4, 2)
monkeyDict[2] = Monkey(2, [74, 87], 2, "+", 5, 7, 4)
monkeyDict[3] = Monkey(3, [53, 81, 60, 87, 90, 99, 75], 1, "+", 2, 2, 1)
monkeyDict[4] = Monkey(4, [57], 6, "+", 13, 7, 0)
monkeyDict[5] = Monkey(5, [54, 84, 91, 55, 59, 72, 75, 70], 0, "**", 7, 6, 3)
monkeyDict[6] = Monkey(6, [95, 79, 79, 68, 78], 3, "+", 3, 1, 3)
monkeyDict[7] = Monkey(7, [61, 97, 67], 4, "+", 17, 0, 5)
# get a copy of the data for part two
monkeyDict2 = copy.deepcopy(monkeyDict)

for i in range(20):
    for monkey in monkeyDict.values():
        monkey.passItems(1, monkeyDict)
most_active = sorted([monkey.inspected for monkey in monkeyDict.values()])[-2:]
print(f"Part one: {most_active[0] * most_active[1]}")

for i in range(10_000):
    for monkey in monkeyDict2.values():
        monkey.passItems(2, monkeyDict2)
most_active = sorted(
    [monkey.inspected for monkey in monkeyDict2.values()])[-2:]
print(f"Part two: {most_active[0] * most_active[1]}")
