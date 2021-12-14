import sys
import itertools
from collections import Counter, defaultdict

template = sys.stdin.readline().strip()

sys.stdin.readline()

rules = {}

for line in sys.stdin.readlines():
    left, right = line.strip().split(' -> ')
    rules[left] = right

pairs = Counter(map(lambda p: ''.join(p), zip(template, template[1:])))

for _ in range(40):
    new_pairs = Counter()

    for pair, count in pairs.items():
        new_pairs[pair[0] + rules[pair]] += count
        new_pairs[rules[pair] + pair[1]] += count
    pairs = new_pairs

letter_counts = Counter()

# Count just the beginning letter
for pair, count in pairs.items():
    letter_counts[pair[0]] += count
# end of sequence letter counted once more
letter_counts[template[-1]] += 1

ordered = sorted(letter_counts.items(), key=lambda i: i[1])

print(ordered[-1][1] - ordered[0][1])
