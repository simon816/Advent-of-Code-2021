import sys

grid = []

for line in sys.stdin.readlines():
    grid.append([int(n) for n in line.strip()])

out = 0

for y, row in enumerate(grid):
    for x, n in enumerate(row):
        look = []
        if x > 0:
            look.append(row[x - 1])
        if x < len(row) - 1:
            look.append(row[x + 1])
        if y > 0:
            look.append(grid[y - 1][x])
        if y < len(grid) - 1:
            look.append(grid[y + 1][x])
        if n < min(look):
            out += 1 + n
print(out)
