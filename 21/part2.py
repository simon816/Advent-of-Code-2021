import sys
import itertools
import functools
from collections import Counter

p1 = sys.stdin.readline().strip()
pos1 = int(p1[p1.index(': ') + 2:])
p2 = sys.stdin.readline().strip()
pos2 = int(p2[p2.index(': ') + 2:])

def fixup(n):
    if n > 10:
        n = n % 10
        if n == 0:
            n = 10
    return n

def get_results(base, start_score):
    for a in range(base+1, base+4):
        a = fixup(a)
        for b in range(a+1, a+4):
            b = fixup(b)
            for c in range(b+1, b+4):
                c = fixup(c)
                yield c, start_score + c

def get_counts(pos, score):
    c = Counter()
    for new_pos, new_score in get_results(pos, score):
        c[(new_pos, new_score)] += 1
    return c

# yields (p1_state, p2_state), num_occurences
def get_state_count(p1_pos, p1_score, p2_pos, p2_score):
    p1_counts = get_counts(p1_pos, p1_score).items()
    p2_counts = get_counts(p2_pos, p2_score).items()
    pr = itertools.product(p1_counts, p2_counts)
    p1_win_states = set()
    for ((np1_pos, np1_score), p1_count), ((np2_pos, np2_score), p2_count) in pr:
        # If p1 wins, the game stops and p2 does not get to move
        if np1_score >= 21:
            state = (np1_pos, np1_score), (p2_pos, p2_score)
            if state not in p1_win_states:
                p1_win_states.add(state)
                yield state + (p1_count,)
        else:
            p2_win_count = p2_count if np2_score >= 21 else 0
            yield (np1_pos, np1_score), (np2_pos, np2_score), p1_count * p2_count


@functools.lru_cache(maxsize=None)
def get_num_universes(p1_pos, p1_score, p2_pos, p2_score):
    if p1_score >= 21:
        return 1, 0
    elif p2_score >= 21:
        return 0, 1
    p1_win_total = 0
    p2_win_total = 0
    for (p1_pos, p1_score), (p2_pos, p2_score), count in get_state_count(
        p1_pos, p1_score, p2_pos, p2_score):
        p1_wins, p2_wins = get_num_universes(p1_pos, p1_score, p2_pos, p2_score)
        p1_win_total += count * p1_wins
        p2_win_total += count * p2_wins
    return p1_win_total, p2_win_total

print(max(get_num_universes(pos1, 0, pos2, 0)))
