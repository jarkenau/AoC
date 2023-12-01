import ast

pairs = [item.split('\n') for item in open("input.txt").read().strip().split('\n\n')]

# ast.literal_eval() is safer than plain eval(), https://stackoverflow.com/a/15197726
packet_pairs = [[ast.literal_eval(packet) for packet in pairs] for pairs in pairs]

packets = [item for pair in packet_pairs for item in pair]

# use recursion to compare the packets
def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            if diff := compare(l, r):
                return diff
        return len(left) - len(right)
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])

indices = []
for index, (left, right) in enumerate(packet_pairs, 1):
    if compare(left, right) < 0:
        indices.append(index)
    
print(f"Part one: {sum(indices)}")

def find_dividers(packets: list, divider: list) -> int:
    # count the number of packets that are smaller than the divider
    return sum(compare(packet, divider) <= 0 for packet in packets)

dividers =  [[[2]], [[6]]]
packets += dividers

product = 1
for divider in dividers:
    product *= find_dividers(packets, divider)

print(f"Part two: {product}")