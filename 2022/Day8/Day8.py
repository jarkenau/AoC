grid = [[int(height) for height in line] for line in open("input.txt").read().strip().splitlines()]

# https://stackoverflow.com/questions/34386476/how-to-loop-through-a-column-in-python
gridT = list(zip(*grid)) # transpose matrix without numpy

# visible from the outside
visible = 2* (len(grid[0]) -1) + 2 * (len(grid) - 1)

for row in range(1, len(grid[0]) - 1):
    for column in range(1, len(grid) -  1):
        treeHeight = grid[row][column]
        left = [treeHeight > height for height in grid[row][:column]]
        right = [treeHeight > height for height in grid[row][column+1:]]
        top = [treeHeight > height for height in gridT[column][:row]]
        bottom = [treeHeight > height for height in gridT[column][row+1:]]
        if all(left) or all(right) or all(top) or all(bottom):
            visible += 1

assert(visible == 1801)
print(f"Visible trees: {visible}")

def viewLength(treeHeight: int, otherTrees: list) -> int:
    length = 0
    for height in otherTrees:
        length += 1
        if height >= treeHeight:
            break
    return length

score = 0
for row in range(len(grid[0])):
    for column in range(len(grid)):
        treeHeight = grid[row][column]
        sToLeft = viewLength(treeHeight, grid[row][0:column][::-1])
        sToRight = viewLength(treeHeight, grid[row][column + 1:])
        sToTop = viewLength(treeHeight, gridT[column][0:row][::-1])
        sToBottom = viewLength(treeHeight, gridT[column][row + 1:])
        totalSum = sToLeft * sToRight * sToTop * sToBottom
        if totalSum > score :
            score = totalSum

assert(score == 209880)
print(f"Highest score: {score}")

    