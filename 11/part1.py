import sys

grid = []

for line in sys.stdin.readlines():
    grid.append([int(c) for c in line.strip()])

total = 0

for _ in range(100):
    step = True
    skip = set()
    while True:
        flashed = False
        for i, row in enumerate(grid):
            flash = []
            for j, n in enumerate(row):
                if step:
                    row[j] += 1
                if row[j] >= 10 and (i, j) not in skip:
                    skip.add((i, j))
                    flash.append(j)
                    row[j] = 0
                    flashed = True
            for f in flash:
                if i > 0:
                    if f > 0 and (i-1, f-1) not in skip:
                        grid[i - 1][f - 1] += 1
                    if (i-1,f) not in skip:
                        grid[i - 1][f] += 1
                    if f < len(row) - 1 and (i-1,f+1) not in skip:
                        grid[i - 1][f + 1] += 1
                if i < len(grid) - 1:
                    if f > 0 and (i+1, f-1) not in skip:
                        grid[i + 1][f - 1] += 1
                    if (i+1,f) not in skip:
                        grid[i + 1][f] += 1
                    if f < len(row) - 1:
                        if (i+1,f+1) not in skip:
                            grid[i + 1][f + 1] += 1
                if f > 0 and (i, f-1) not in skip:
                    row[f - 1] += 1
                if f < len(row) - 1 and (i,f+1) not in skip:
                    row[f + 1] += 1
        step = False
        if not flashed:
            break
    total += len(skip)

print(total)
