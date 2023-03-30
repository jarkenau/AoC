from collections import deque, defaultdict
import numpy as np

map = [list(line) for line in open('input.txt').read().splitlines()]

# get dimensions of the map
n, m = len(map), len(map[0])

sx, sy = list(zip(*np.where(np.array(map) == "S")))[0]
tx, ty = list(zip(*np.where(np.array(map) == "E")))[0]

# convert the start and end the corresponding height letters
map[sx][sy] = "a"
map[tx][ty] = "z"

# convert the letters to numbers
map = [[ord(c) - ord("a") for c in r] for r in map]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# use bfs to find the shortest path
queue_part_one = deque([(sx, sy)])
queue_part_two = deque(list(zip(*np.where(np.array(map) == 0))))

# keep track of the distance to each entry/node
distance_part_one = defaultdict(lambda: 10_000)
distance_part_two = defaultdict(lambda: 10_000)

distance_part_one[sx, sy] = 0
for sx, sy in queue_part_two:
    distance_part_two[sx, sy] = 0

def find_shortest_path(map: list[list[int]], queue: deque, distance: defaultdict) -> int:
    while len(queue) > 0:
        cx, cy = queue.popleft()
        # found the end
        if (cx, cy) == (tx, ty):
            return distance[cx, cy]
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # are we still in the map?
            if nx in range(n) and ny in range(m):
                if map[cx][cy] >= map[nx][ny] - 1:
                    new_distance = distance[cx, cy] + 1
                    if new_distance < distance[nx, ny]:
                        distance[nx, ny] = new_distance
                        queue.append((nx, ny))

print(f"Min distance part one: {find_shortest_path(map, queue_part_one, distance_part_one)}")
print(f"Min distance part two: {find_shortest_path(map, queue_part_two, distance_part_two)}")