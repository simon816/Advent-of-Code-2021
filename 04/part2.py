import re
import sys

lines = sys.stdin.readlines()

numbers = [int(n) for n in lines[0].strip().split(',')]

grids = []

grid = []
for line in lines[2:]:
    line = line.strip()
    if not line:
        grids.append(grid)
        grid = []
        continue
    grid.append([(int(n), False) for n in re.split('\s+', line)])

for num in numbers:
    new_grids = []
    for grid in grids:
        columns_complete = [True] * 5
        for row in grid:
            row_complete = True
            for col, (val, marked) in enumerate(row):
                if val == num:
                    marked = True
                row[col] = (val, marked)
                if not marked:
                    row_complete = False
                    columns_complete[col] = False
            if row_complete:
                break
        win = row_complete or all(columns_complete)
        if not win:
            new_grids.append(grid)
    if not new_grids:
        last_grid = grids[0]
        break
    grids = new_grids

print(sum(v for row in last_grid for (v, marked) in row if not marked) * num)
