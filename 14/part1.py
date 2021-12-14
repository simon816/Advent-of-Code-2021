import sys
import itertools

template = sys.stdin.readline().strip()

sys.stdin.readline()

rules = {}

for line in sys.stdin.readlines():
    left, right = line.strip().split(' -> ')
    rules[left] = right

s = template
for _ in range(10):
    new_s = ''
    for pair in zip(s, s[1:]):
        new_s += pair[0] + rules[''.join(pair)]
    s = new_s + pair[1]

count = {}
for p in s:
    if p not in count:
        count[p] = s.count(p)


ordered = sorted(count.items(), key=lambda i: i[1])

print(ordered[-1][1] - ordered[0][1])
