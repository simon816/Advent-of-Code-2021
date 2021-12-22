import sys
import itertools

p1 = sys.stdin.readline().strip()
pos1 = int(p1[p1.index(': ') + 2:])
p2 = sys.stdin.readline().strip()
pos2 = int(p2[p2.index(': ') + 2:])

die = itertools.cycle(range(1, 101))

scores = {
    1: 0,
    2: 0,
}
positions = {
    1: pos1,
    2: pos2,
}

rolls = 0
loser = None
while loser is None:
    for player in positions.keys():
        roll = next(die) + next(die) + next(die)
        rolls += 3
        new_pos = (positions[player] + roll) % 10
        if new_pos == 0:
            new_pos = 10
        positions[player] = new_pos
        scores[player] += new_pos
        if scores[player] >= 1000:
            loser = 2 if player == 1 else 1
            break
print(scores[loser] * rolls)
