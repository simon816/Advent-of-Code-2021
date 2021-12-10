import sys

pair_map = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

score_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
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
        score += score_map[corrupt]

print(score)
