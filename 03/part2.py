from collections import Counter, defaultdict
import sys

def update_filter(values, func):
    counters = defaultdict(lambda: Counter())
    for num in values:
        for i, n in enumerate(num):
            counters[i][n] += 1
    filter = {}
    for i in sorted(counters.keys()):
        zero = counters[i].get(0, 0)
        one = counters[i].get(1, 0)
        filter[i] = func(zero, one)
    return filter

if __name__ == '__main__':
    values = [[int(n) for n in line.strip()] for line in sys.stdin.readlines()]
    ox_vals = list(values)
    co2_vals = list(values)
    for b in range(max(map(len, values))):
        ox_filter = update_filter(ox_vals, lambda zero, one: 0 if zero > one else 1)
        co2_filter = update_filter(co2_vals, lambda zero, one: 1 if one < zero else 0)
        if len(ox_vals) > 1:
            ox_vals = [n for n in ox_vals if n[b] == ox_filter[b]]
        if len(co2_vals) > 1:
            co2_vals = [n for n in co2_vals if n[b] == co2_filter[b]]
    assert len(ox_vals) == 1
    assert len(co2_vals) == 1
    # lazy binary to decimal conversion
    ox = int(''.join(map(str, ox_vals[0])), 2)
    co2 = int(''.join(map(str, co2_vals[0])), 2)
    print(ox * co2)
