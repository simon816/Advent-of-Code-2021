import sys

def distance(a, b):
    d = []
    for a1, b1 in zip(a, b):
        d.append(abs(a1 - b1))
    return tuple(sorted(d))

def rotate(point, count, axis):
    p = list(point)
    for _ in range(count):
        if axis == 1:
            # +z -> +x
            # -z -> -x
            # +x -> -z
            # -x -> +z
            p[0], p[2] = p[2], -p[0]
        elif axis == 0:
            # +y -> -z
            # -y -> +z
            # -z -> -y
            # +z -> +y
            p[2], p[1] = -p[1], p[2]
        elif axis == 2:
            # +x -> -y
            # -x -> +y
            # +y -> +x
            # -y -> -x
            p[1], p[0] = -p[0], p[1]
        else:
            assert False
    return tuple(p)

scanners = {}

scanner = None
for line in sys.stdin.readlines():
    line = line.strip()
    if line.startswith('---'):
        scanner = int(line[len('--- scanner '):line.rindex('---')])
        assert scanner not in scanners
        scanners[scanner] = []
    elif line:
        coord = tuple(map(int, line.split(',')))
        scanners[scanner].append(coord)

base = set(scanners[0])
del scanners[0]

def rotate_points(points, count, axis):
    return [rotate(point, count, axis) for point in points]

def rotate_about(points, axis):
    for r in range(4):
        yield rotate_points(points, r, axis)

while scanners:
    found = None
    found_offset = None
    for scanner, other in scanners.items():
        candidate_sets = []
        points = other
        candidate_sets.extend(rotate_about(points, 0))
        points = rotate_points(points, 1, 1)
        candidate_sets.extend(rotate_about(points, 2))
        points = rotate_points(points, 1, 1)
        candidate_sets.extend(rotate_about(points, 0))
        points = rotate_points(points, 1, 1)
        candidate_sets.extend(rotate_about(points, 2))
        points = rotate_points(points, 1, 0)
        candidate_sets.extend(rotate_about(points, 1))
        points = rotate_points(points, 2, 0)
        candidate_sets.extend(rotate_about(points, 1))
        for point in base:
            for candidate in candidate_sets:
                for c_point in candidate:
                    ox = c_point[0] - point[0]
                    oy = c_point[1] - point[1]
                    oz = c_point[2] - point[2]
                    found_offset = -ox, -oy, -oz
                    new_points = []
                    match_count = 0
                    for other_cpoint in candidate:
                        new_point = (
                            other_cpoint[0] - ox,
                            other_cpoint[1] - oy,
                            other_cpoint[2] - oz,
                        )
                        if new_point in base:
                            match_count += 1
                        new_points.append(new_point)
                    if match_count >= 12:
                        found = new_points
                        break
                if found is not None:
                    break
            if found is not None:
                break
        if found is not None:
            break
    assert found is not None
    base.update(found)
    del scanners[scanner]

print(len(base))
