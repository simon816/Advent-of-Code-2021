import sys

grid = []

for line in sys.stdin.readlines():
    grid.append([int(n) for n in line.strip()])

part_of = {}

for y, row in enumerate(grid):
    for x, n in enumerate(row):
        if n == 9:
            continue
        if x < len(row) - 1:
            if row[x + 1] < n:
                part_of[(y, x)] = (y, x + 1)
                continue
        if y < len(grid) - 1:
            if grid[y + 1][x] < n:
                part_of[(y, x)] = (y + 1, x)
                continue
        if x > 0:
            if row[x - 1] < n:
                part_of[(y, x)] = (y, x - 1)
                continue
        if y > 0:
            if grid[y - 1][x] < n:
                part_of[(y, x)] = (y - 1, x)
                continue
basins = {}
basin_sizes = {}
b_id = 0

for k, v in part_of.items():
    trace = []
    t = v
    while t in part_of:
        t = part_of[t]
    if t not in basins:
        b = basins[t] = b_id
        basin_sizes[b] = 1
        b_id += 1
    else:
        b = basins[t]
    basin_sizes[b] += 1

sizes = sorted(basin_sizes.values())
print(sizes[-1] * sizes[-2] * sizes[-3])
