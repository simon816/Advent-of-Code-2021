import sys

fish = [int(n) for n in sys.stdin.readline().strip().split(',')]

states = {i:fish.count(i) for i in range(9)}
for _ in range(256):
    zero_count = states[0]
    for i in range(0, 8):
        states[i] = states[i + 1]
    states[8] = zero_count
    states[6] += zero_count

print(sum(states.values()))
