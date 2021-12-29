import sys

ordered = []

for line in sys.stdin.readlines():
    start, end = tuple(tuple(map(int, n.split(','))) for n in line.strip().split(' -> '))
    if end[0] < start[0]:
        start, end = end, start
    if start[0] == end[0] or start[1] == end[1]:
        ordered.append((start, end))

ordered = sorted(ordered)

sz = 1000

traces = [[] for _ in range(sz)]

out = 0

for x in range(sz):
    while len(ordered) and ordered[0][0][0] == x:
        ((x1, y1), (x2, y2)) = ordered.pop(0)
        for y in range(min(y1, y2), max(y1, y2) + 1):
            traces[y].append(x2)
    for y in range(sz):
        active_count = len(traces[y])
        if active_count > 1:
            out += 1
        traces[y] = [end for end in traces[y] if end > x]

print(out)
