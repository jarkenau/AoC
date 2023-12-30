from typing import List
from collections import Counter


def hand_type(hand: str, enable_jokers: bool = False) -> int:
    """Return a numeric value or each hand type"""
    c = Counter(hand)
    # the most efficient use of a joker is to add them to the most common non-joker card
    if enable_jokers:
        counts = None
        num_jokers = c.pop("J", 0)
        if num_jokers == 5:
            counts = [5]
        else:
            counts = sorted(c.values())
            counts[-1] += num_jokers
    else:
        counts = list(c.values())
    if 5 in counts:
        return 7
    if 4 in counts:
        return 6
    if 3 in counts:
        if 2 in counts:
            return 5
        return 4
    if counts.count(2) == 2:
        return 3
    if 2 in counts:
        return 2
    return 1


def card_strength(hand: str, ordering: str) -> List[int]:
    """Return the relative strength of each card in the hand"""
    return list(map(ordering.index, hand))


plays = [line.strip().split() for line in open("input.txt").readlines()]

part_one_sorted = sorted(
    plays, key=lambda x: (hand_type(x[0]), card_strength(x[0], "23456789TJQKA"))
)
part_two_sorted = sorted(
    plays,
    key=lambda x: (
        hand_type(x[0], enable_jokers=True),
        card_strength(x[0], "J23456789TQKA"),
    ),
)

part_one, part_two = [
    sum(int(play[1]) * i for i, play in enumerate(part_sorted, 1))
    for part_sorted in [part_one_sorted, part_two_sorted]
]

print(f"Part One: {part_one}")
print(f"Part Two: {part_two}")