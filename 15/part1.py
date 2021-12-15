import sys

nodes = {}
costs = {}

y = 0
max_x = 0

lines = list(sys.stdin.readlines())
for line in lines:
    risks = [int(n) for n in line.strip()]
    for x, risk in enumerate(risks):
        max_x = max(x, max_x)
        a = []
        if x > 0:
            a.append((x-1, y))
        if x < len(risks) - 1:
            a.append((x+1, y))
        if y > 0:
            a.append((x, y-1))
        if y < len(lines) - 1:
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
while node != dest:
    curr_dist = weights[node] = min(curr_dist, weights[node])
    permanents.add(node)
    for adj in nodes[node]:
        if adj in permanents:
            continue
        if adj in weights:
            weights[adj] = min(weights[adj], curr_dist + costs[adj])
        else:
            weights[adj] = curr_dist + costs[adj]
    non_perms = list(filter(lambda e: e[0] not in permanents, weights.items()))
    assert non_perms, "No Route!"
    lowest = min(map(lambda e: e[1], non_perms))
    matching = filter(lambda e: e[1] == lowest, non_perms)
    node = next(matching)[0]
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
