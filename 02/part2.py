import sys

if __name__ == '__main__':

    h = 0
    d = 0
    aim = 0

    for line in sys.stdin.readlines():
        dir, val = line.strip().split(' ')
        val = int(val)
        if dir == 'up':
            aim -= val
        elif dir == 'down':
            aim += val
        elif dir == 'forward':
            h += val
            d += aim * val
    print(h * d)
