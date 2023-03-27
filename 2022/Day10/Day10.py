x_register, signal_strength, crt = 1, 0, "\n"

split_instructions = [instruction for instruction in open("input.txt").read().split()]

for cycle, inc in enumerate(split_instructions, 1):
    if cycle % 40 == 20:
        signal_strength += x_register * cycle
    if abs((cycle - 1) % 40 - x_register) < 2:
        crt += '#'
    elif cycle % 40 == 0:
        crt += '\n'
    else:
        crt += '.'
    if inc.lstrip('-').isdigit():
        x_register += int(inc)

print(f"Signal strength: {signal_strength}")
print(*crt)
