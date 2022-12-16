moves = [move.split() for move in open("input.txt").read().strip().splitlines()]

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

def moveHead(head: Point2D, direction: str):
    head.x += 1 if direction == "R" else -1 if direction == "L" else 0
    head.y += 1 if direction == "U" else -1 if direction == "D" else 0

def followHead(tail: Point2D, head: Point2D):
    if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
        tail.x += 1 if head.x > tail.x else -1 if head.x < tail.x else 0
        tail.y += 1 if head.y > tail.y else -1 if head.y < tail.y else 0

def ropeMoves(ropeLength: int) -> int:
    setOfMoves = set()
    position = [Point2D(0, 0) for _ in range(ropeLength)]
    for directionStr, lengthStr in moves:
        for _ in range(int(lengthStr)):
            moveHead(position[0], directionStr)
            for i in range(1, ropeLength):
                followHead(position[i], position[i - 1])
            setOfMoves.add((position[ropeLength - 1].x, position[ropeLength - 1].y))
    return len(setOfMoves)

print(f"Number of moves: {ropeMoves(2)}")
print(f"Number of moves: {ropeMoves(10)}")