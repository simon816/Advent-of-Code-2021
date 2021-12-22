import sys

steps = []
for line in sys.stdin.readlines():
    state, coord_range = line.strip().split(' ')
    step = {'state': state}
    for r in coord_range.split(','):
        label, r = r.split('=')
        start, end = tuple(map(int, r.split('..')))
        step[label] = (start, end)
    steps.append(step)

def get_intersection(a, b):
    i = []
    for (a1, a2), (b1, b2) in zip(a, b):
        if a1 > b2 or a2 < b1:
            return None
        start = max(a1, b1)
        end = min(a2, b2)
        i.append((start, end))
    return tuple(i)

def split_by_intersection(cube, intersection):
    new_cubes = []
    (cx1, cx2), (cy1, cy2), (cz1, cz2) = cube
    (ix1, ix2), (iy1, iy2), (iz1, iz2) = intersection
    # +1 or -1 because intersection is inclusive
    bottom_height = iy1 - cy1
    if bottom_height:
        new_cubes.append(((cx1, cx2), (cy1, iy1-1), (cz1, cz2)))
    top_height = cy2 - iy2
    if top_height:
        new_cubes.append(((cx1, cx2), (iy2+1, cy2), (cz1, cz2)))
    left_width = ix1 - cx1
    if left_width:
        new_cubes.append(((cx1, ix1-1), (iy1, iy2), (cz1, cz2)))
    right_width = cx2 - ix2
    if right_width:
        new_cubes.append(((ix2+1, cx2), (iy1, iy2), (cz1, cz2)))
    front_depth = iz1 - cz1
    if front_depth:
        new_cubes.append(((ix1, ix2), (iy1, iy2), (cz1, iz1-1)))
    rear_depth = cz2 - iz2
    if rear_depth:
        new_cubes.append(((ix1, ix2), (iy1, iy2), (iz2+1, cz2)))
    return new_cubes

def r_len(r):
    # +1 because inclusive
    return 1 + abs(r[1] - r[0])

def c_vol(c):
    return r_len(c[0]) * r_len(c[1]) * r_len(c[2])

disjoint_cuboids = set()

for step in steps:
    is_on, our_cube = step['state'] == 'on', (step['x'], step['y'], step['z'])
    new_cubes = set()
    old_cubes = set()
    did_intersect = False
    for cube in disjoint_cuboids:
        i = get_intersection(our_cube, cube)
        if i is not None:
            did_intersect = True
            resultant_other_cubes = split_by_intersection(cube, i)
            new_cubes.update(resultant_other_cubes)
            old_cubes.add(cube)
    for c in old_cubes:
        disjoint_cuboids.remove(c)
    disjoint_cuboids.update(new_cubes)
    if is_on:
        disjoint_cuboids.add(our_cube)

print(sum(map(c_vol, disjoint_cuboids)))
