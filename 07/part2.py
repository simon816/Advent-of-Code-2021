import sys

l = [int(n) for n in sys.stdin.readline().split(',')]

# I'm sure there's better ways
def do():
    for s in set(range(max(l) + 1)):
        su = 0
        for n in l:
            fuel = 0
            dist = abs(n - s)
            cost = 1
            for _ in range(dist):
                fuel += cost
                cost += 1
            su += fuel
        yield su

print(min(do()))
            
