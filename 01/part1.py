import sys
import itertools

if __name__ == '__main__':

    values = [int(line.strip()) for line in sys.stdin.readlines()]
    prev = None
    inc = 0
    for v in values:
        if prev is not None and v > prev:
            inc += 1
        prev = v
    print(inc)
