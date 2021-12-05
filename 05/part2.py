import sys

grid = []

for line in sys.stdin.readlines():
    start, end = tuple(tuple(map(int, n.split(','))) for n in line.strip().split(' -> '))
    # populate grid up to max y if absent
    max_x = max(start[0], end[0])
    max_y = max(start[1], end[1])
    for y in range(max_y + 1):
        if len(grid) <= y:
            grid.append([0 for _ in range(max_x + 1)])
        else:
            grid[y].extend(0 for _ in range(max_x - (len(grid[y]) - 1)))
    if start[0] == end[0]: # x1 == x2
        lower_y = min(start[1], end[1])
        upper_y = max(start[1], end[1])
        for y in range(lower_y, upper_y + 1):
            grid[y][start[0]] += 1
    elif start[1] == end[1]: # y1 == y2
        lower_x = min(start[0], end[0])
        upper_x = max(start[0], end[0])
        for x in range(lower_x,  upper_x + 1):
            grid[start[1]][x] += 1
    else:
        start_y = start[1]
        end_y = end[1]
        x = start[0]
        for y in range(start_y, end_y + (1 if end_y >= start_y else -1), 1 if end_y >= start_y else -1):
            grid[y][x] += 1
            x += 1 if start[0] <= end[0] else -1

print(len([c for row in grid for c in row if c > 1]))

