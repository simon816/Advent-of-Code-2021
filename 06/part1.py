import sys

fish = [int(n) for n in sys.stdin.readline().strip().split(',')]

for _ in range(80):
    for i in range(len(fish)):
        next = fish[i] - 1
        if fish[i] == 0:
            next = 6
            fish.append(8)
        fish[i] = next
print(len(fish))
