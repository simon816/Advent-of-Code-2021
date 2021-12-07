import sys

l = [int(n) for n in sys.stdin.readline().split(',')]

print(min(sum(abs(n - s) for n in l) for s in set(l)))
