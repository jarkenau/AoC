dataStream = [char for char in open("input.txt").read().strip()]

def findMarker(data: list, distinctChars: int) -> int:
    for leftIndex in range(len(data) - distinctChars):
        rightIndex = leftIndex + distinctChars
        if len((set(data[leftIndex:rightIndex]))) == distinctChars:
            return rightIndex
    return None

marker = findMarker(dataStream, 4)

assert(marker == 1598)
print(f"First solution: {marker}")

marker = findMarker(dataStream, 14)

assert(marker == 2414)
print(f"Second solution: {marker}")
        