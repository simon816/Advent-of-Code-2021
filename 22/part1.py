import sys

steps = []
for line in sys.stdin.readlines():
    state, coord_range = line.strip().split(' ')
    step = {'state': state}
    skip = False
    for r in coord_range.split(','):
        label, r = r.split('=')
        start, end = tuple(map(int, r.split('..')))
        step[label] = (start, end)
        if start < -50 or end < -50 or start > 50 or end > 50:
            skip = True
    if not skip:
        steps.append(step)

on = set()

for s in steps:
    for x in range(s['x'][0], s['x'][1] + 1):
        for y in range(s['y'][0], s['y'][1] + 1):
            for z in range(s['z'][0], s['z'][1] + 1):
                coord = (x, y, z)
                if s['state'] == 'on':
                    on.add(coord)
                elif coord in on:
                    on.remove(coord)

print(len(on))
