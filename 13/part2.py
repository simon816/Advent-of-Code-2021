import sys

coords = True

grid = []
size_x = 0
size_y = 0

folds = []

for line in sys.stdin.readlines():
    l = line.strip()
    if not l and coords:
        coords = False

    if coords:
        x, y = (int(n) for n in l.split(','))
        size_x = max(x, size_x)
        size_y = max(y, size_y)
        for _ in range(len(grid) - 1, y):
            grid.append([])
        row = grid[y]
        for _ in range(len(row) - 1, x):
            row.append(0)
        row[x] = 1
    elif l:
        fold = line[len('fold along '):].split('=')
        axis, pos = fold[0], int(fold[1])
        folds.append((axis, pos))

for row in grid:
    for _ in range(len(row) - 1, size_x):
        row.append(0)

def merge(source, dest):
    for i in range(len(dest)):
        dest[i] |= source[i]

def fold_y(pos):
    global grid
    for y in range(1, (size_y - pos) + 1):
        if pos - y < 0:
            break
        merge(grid[pos + y], grid[pos - y])
    grid = grid[:pos]

def fold_x(pos):
    for i, row in enumerate(grid):
        slice = row[pos + 1:]
        slice.reverse()
        new = row[:pos]
        merge(slice, new)
        grid[i] = new

def fold(f):
    axis, pos = f
    if axis == 'y':
        fold_y(pos)
    elif axis == 'x':
        fold_x(pos)
    else:
        assert False

for f in folds:
    fold(f)

for r in grid:
    print(''.join(map(lambda n: '#' if n else '.', r)))
