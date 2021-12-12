import sys
from collections import defaultdict

nodes = defaultdict(list)

for line in sys.stdin.readlines():
    start, end = line.strip().split('-')
    nodes[start].append(end)
    nodes[end].append(start)

def walk(node, path, visited):
    complete = []
    for adj in nodes[node]:
        if adj == 'end':
            complete.append(path + [adj])
            continue
        if adj not in visited:
            more = []
            if adj.lower() == adj:
                more.append(adj)
            for p in walk(adj, path + [adj], visited | set(more)):
                complete.append(p)
    return [p for p in complete if p[-1] == 'end']

print(len(walk('start', [], set(['start']))))
