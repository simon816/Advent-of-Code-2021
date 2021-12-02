import sys

if __name__ == '__main__':

    h = 0
    d = 0

    for line in sys.stdin.readlines():
        dir, val = line.strip().split(' ')
        val = int(val)
        if dir == 'up':
            d -= val
        elif dir == 'down':
            d += val
        elif dir == 'forward':
            h += val
    print(h * d)
