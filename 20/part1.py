import sys

algo = None

finite_image = []
max_width = 0
for line in sys.stdin.readlines():
    l = list(line.strip())
    if not algo:
        assert len(l) == 512
        algo = l
        continue
    if not l:
        continue
    l.insert(0, '.')
    l.append('.')
    finite_image.append(l)
    max_width = max(max_width, len(l))
finite_image.insert(0, ['.'] * max_width)
finite_image.append(['.'] * max_width)

flaps = algo[0] == '#' and algo[511] == '.'
    
def run(image, seq_num):
    if flaps:
        this_empty = seq_num % 2
        next_empty = '#' if this_empty == 0 else '.'
    else:
        this_empty = 0
        next_empty = '.'
    width = len(image[0])
    new_image = [[next_empty] * (width + 2)]
    for y, row in enumerate(image):
        new_row = [next_empty]
        for x in range(len(row)):
            num = 0
            for scan_y in (y - 1, y, y + 1):
                for scan_x in (x - 1, x, x + 1):
                    if scan_y < 0 or scan_y >= len(image):
                        val = this_empty
                    else:
                        r = image[scan_y]
                        if scan_x < 0 or scan_x >= len(r):
                            val = this_empty
                        else:
                            val = 1 if r[scan_x] == '#' else 0
                    num = num << 1
                    num += val
            new_row.append(algo[num])
        new_row.append(next_empty)
        new_image.append(new_row)
    new_image.append([next_empty] * (width + 2))

    return new_image

image = finite_image
for seq in range(2):
    image = run(image, seq)

print(sum(r.count('#') for r in image))
