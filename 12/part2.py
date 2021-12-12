import sys
from collections import defaultdict

nodes = defaultdict(list)

for line in sys.stdin.readlines():
    start, end = line.strip().split('-')
    nodes[start].append(end)
    nodes[end].append(start)

def walk(node, path, visited_count, allowed_counts):
    complete = []
    for adj in nodes[node]:
        if adj == 'end':
            complete.append(path + [adj])
            continue
        if adj not in visited_count or visited_count[adj] < allowed_counts[adj]:
            new = dict(visited_count)
            if adj.lower() == adj:
                if adj in new:
                    new[adj] += 1
                else:
                    new[adj] = 1
            for p in walk(adj, path + [adj], new, allowed_counts):
                complete.append(p)
    return [tuple(p) for p in complete if p[-1] == 'end']

paths = set()

for n in (k for k in nodes.keys() if k.lower() == k and k not in ['start', 'end']):
    allowed_counts = { other: 1 for other in nodes.keys() }
    allowed_counts[n] = 2
    
    paths.update(walk('start', [], {'start': 1}, allowed_counts))

print(len(paths))
