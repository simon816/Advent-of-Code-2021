import sys

_, ranges = sys.stdin.readline().strip().split(':')
xrange, yrange = [tuple(int(v) for v in r.split('=')[1].split('..'))\
                  for r in ranges.split(', ')]

try_vx, try_vy = 1, 1
highest_y = 0

while True:
    x, y = 0, 0
    vx, vy = try_vx, try_vy
    in_range = False
    needs_more_x = False
    needs_less_x = False
    highest_y = 0
    while True:
        x += vx
        y += vy
        highest_y = max(y, highest_y)
        if vx:
            vx += -1 if vx > 0 else 1
        vy -= 1
        in_xrange = x >= xrange[0] and x <= xrange[1]
        in_yrange = y >= yrange[0] and y <= yrange[1]
        if vx == 0 and not in_xrange:
            needs_more_x = x < xrange[0]
            needs_less_x = x > xrange[1]
            break
        if y < yrange[0]:
            break
        if in_xrange and in_yrange:
            in_range = True
            break
    if needs_more_x:
        try_vx += 1
    elif needs_less_x:
        try_vx -= 1
    else:
        try_vy += 1
        # If our vy will overshoot to begin with, break
        if try_vy >= abs(yrange[0]):
            break

print(highest_y)
