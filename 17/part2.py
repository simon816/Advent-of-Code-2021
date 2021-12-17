import sys

_, ranges = sys.stdin.readline().strip().split(':')
xrange, yrange = [tuple(int(v) for v in r.split('=')[1].split('..'))\
                  for r in ranges.split(', ')]

count = 0

for try_vx in range(1, xrange[1] + 1):
    try_vy = yrange[0]
    while True:
        vx, vy = try_vx, try_vy
        x, y = 0, 0
        in_range = False
        impossible_x = False
        impossible_y = False
        while True:
            x += vx
            y += vy
            if vx:
                vx += -1 if vx > 0 else 1
            vy -= 1
            in_xrange = x >= xrange[0] and x <= xrange[1]
            in_yrange = y >= yrange[0] and y <= yrange[1]
            if vx == 0 and not in_xrange:
                impossible_x = True
                break
            if y < yrange[0]:
                break
            if in_xrange and in_yrange:
                in_range = True
                break
        if in_range:
            count += 1
        try_vy += 1
        # If our vy will overshoot to begin with, break
        if try_vy >= abs(yrange[0]):
            break
        if impossible_x or impossible_y:
            break

print(count)
