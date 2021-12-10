import sys

pair_map = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

score_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []

for line in sys.stdin.readlines():
    open_stack = []
    corrupt = None
    for c in line.strip():
        if c in '{[(<':
            open_stack.append(c)
        else:
            assert open_stack
            last = open_stack.pop()
            if pair_map[last] != c:
                corrupt = c
                break
    if corrupt is not None:
        continue
    score = 0
    open_stack.reverse()
    close_order = [pair_map[c] for c in open_stack]
    for c in close_order:
        score *= 5
        score += score_map[c]
    scores.append(score)

print(sorted(scores)[len(scores) // 2])
