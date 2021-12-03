from collections import Counter, defaultdict
import sys

if __name__ == '__main__':
    counters = defaultdict(lambda: Counter())
    for line in sys.stdin.readlines():
        for i, n in enumerate(line.strip()):
            counters[i][n] += 1
    gamma = ''
    epsilon = ''
    for i in sorted(counters.keys()):
        most, _ = counters[i].most_common(1)[0]
        gamma += most
        epsilon += '1' if most == '0' else '0'
    print(int(gamma, 2) * int(epsilon, 2))
