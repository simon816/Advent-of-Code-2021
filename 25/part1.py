import sys

grid = []

for line in sys.stdin.readlines():
    grid.append([c for c in line.strip()])


def rebuild(new_grid):
    grid = []
    for y in sorted(new_grid.keys()):
        row = []
        for x in sorted(new_grid[y].keys()):
            row.append(new_grid[y][x])
        grid.append(row)
    return grid

moved = True
steps = 0
while moved:
    moved = False
    new_grid = {}
    for y, row in enumerate(grid):
        new_row = {}
        for x, cell in enumerate(row):
            if cell == '>':
                if x == len(row) - 1:
                    if row[0] == '.':
                        moved = True
                        new_row[0] = '>'
                        new_row[x] = '.'
                    else:
                        new_row[x] = '>'
                else:
                    if row[x+1] == '.':
                        moved = True
                        new_row[x+1] = '>'
                        new_row[x] = '.'
                    else:
                        new_row[x] = '>'
            else:
                if x not in new_row:
                    new_row[x] = cell
        if y in new_grid:
            new_row.update(new_grid[y])
        new_grid[y] = new_row
    grid = rebuild(new_grid)
    new_grid = {}
    for y, row in enumerate(grid):
        new_row = {}
        for x, cell in enumerate(row):
            if cell == 'v':
                if y == len(grid) - 1:
                    if grid[0][x] == '.':
                        moved = True
                        new_grid[0][x] = 'v'
                        new_row[x] = '.'
                    else:
                        new_row[x] = 'v'
                else:
                    if grid[y+1][x] == '.':
                        moved = True
                        if y+1 not in new_grid:
                            new_grid[y+1] = {}
                        new_grid[y+1][x] = 'v'
                        new_row[x] = '.'
                    else:
                        new_row[x] = 'v'
            else:
                if x not in new_row:
                    new_row[x] = cell
        if y in new_grid:
            new_row.update(new_grid[y])
        new_grid[y] = new_row
    grid = rebuild(new_grid)
    steps += 1

print(steps)
