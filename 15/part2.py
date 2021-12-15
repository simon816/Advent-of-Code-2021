import sys

nodes = {}
costs = {}

orig = [[int(n) for n in line.strip()] for line in sys.stdin.readlines()]

def calc(n):
    if n > 9:
        return n % 9
    return n

clusters = {}

for y in range(5):
    for x in range(y, y + 5):
        offset = max(x, y)
        new = [ [ calc(n + offset) for n in r] for r in orig ]
        clusters[(x - y, y)] = new

full_grid = []

for y in range(5):
    iters = []
    for x in range(5):
        iters.append(iter(clusters[(x, y)]))
    while True:
        full_row = []
        for i in iters:
            try:
                full_row.extend(next(i))
            except StopIteration:
                break
        if not full_row:
            break
        full_grid.append(full_row)

y = 0
max_x = 0

for risks in full_grid:
    for x, risk in enumerate(risks):
        max_x = max(x, max_x)
        a = []
        if x > 0:
            a.append((x-1, y))
        if x < len(risks) - 1:
            a.append((x+1, y))
        if y > 0:
            a.append((x, y-1))
        if y < len(full_grid) - 1:
            a.append((x, y+1))
        nodes[(x, y)] = a
        costs[(x, y)] = risk
    y += 1

permanents = set()
src = (0, 0)
dest = (max_x, y - 1)
curr_dist = 0
node = src
weights = {src:0}
non_perms = set(nodes.keys())
while node != dest:
    curr_dist = weights[node] = min(curr_dist, weights[node])
    permanents.add(node)
    non_perms.remove(node)
    for adj in nodes[node]:
        if adj in permanents:
            continue
        if adj in weights:
            weights[adj] = min(weights[adj], curr_dist + costs[adj])
        else:
            weights[adj] = curr_dist + costs[adj]
    assert non_perms, "No Route!"
    lowest = None
    low_weight = None
    for n in non_perms:
        if n not in weights:
            continue
        if lowest is None or low_weight > weights[n]:
            lowest = n
            low_weight = weights[n]
    assert lowest is not None
    node = lowest
    curr_dist += costs[node]

permanents.add(dest)
weights[dest] = curr_dist
node = dest
total_risk = 0
while node != src:
    permanents.remove(node)
    total_risk += costs[node]
    dist = weights[node]
    perm_adj = list(filter(lambda a: a in permanents, nodes[node]))
    lowest = min(map(lambda n: weights[n], perm_adj))
    matching = filter(lambda n: weights[n] == lowest, perm_adj)
    node = next(matching)

print(total_risk)
