import sys

def intersect(real, pos, s):
    if pos in real:
        real[pos] = real[pos] & s
    else:
        real[pos] = s
    for other in real.keys():
        if other != pos and len(real[pos]) == 1:
            real[other] = real[other] - real[pos]

def all_elim(real):
    progress = True
    while progress:
        progress = False
        for pos, fin in real.items():
            if len(fin) != 1:
                continue
            for other in real.keys():
                if other != pos:
                    orig = real[other]
                    real[other] = orig - real[pos]
                    if real[other] != orig:
                        progress = True
            

decimals = {
    0: set('abcefg'),
    1: set('cf'),
    2: set('acdeg'),
    3: set('acdfg'),
    4: set('bcdf'),
    5: set('abdfg'),
    6: set('abdefg'),
    7: set('acf'),
    8: set('abcdefg'),
    9: set('abcdfg'),
}

out = 0

for line in sys.stdin.readlines():
    patterns, output = line.strip().split('|')
    patterns = patterns.strip().split(' ')
    output = output.strip().split(' ')

    real = {}
    alldigits = patterns + output
    one = None
    for digit in alldigits:
        s = set(digit)
        if len(digit) == 2:
            one = s
            break
    for digit in alldigits:
        s = set(digit)
        if len(digit) == 3:
            real['a'] = s - one

    for digit in alldigits:
        s = set(digit)
        if len(digit) == 2:
            intersect(real, 'c', s)
            intersect(real, 'f', s)
        elif len(digit) == 3:
            intersect(real, 'c', s)
            intersect(real, 'f', s)
            intersect(real, 'a', s)
        elif len(digit) == 4:
            intersect(real, 'b', s)
            intersect(real, 'c', s)
            intersect(real, 'd', s)
            intersect(real, 'f', s)
        elif len(digit) == 7:
            intersect(real, 'a', s)
            intersect(real, 'b', s)
            intersect(real, 'c', s)
            intersect(real, 'd', s)
            intersect(real, 'e', s)
            intersect(real, 'f', s)
            intersect(real, 'g', s)

    three = None
    six_digits = set()
    for digit in alldigits:
        s = set(digit)
        if len(digit) == 5:
            if s & one == one:
                # this must be a 3
                three = s
                intersect(real, 'a', s)
                intersect(real, 'd', s)
                intersect(real, 'g', s)
        if len(digit) == 6:
            six_digits.add(frozenset(s))
    six = None
    for d in six_digits:
        if len(d - real['c'] - real['f']) == 5:
            six = d
    real['c'] = real['c'] - six
    real['f'] = real['f'] - real['c']
    all_elim(real)
    mapping = {}
    for k in real.keys():
        assert len(real[k]) == 1
        d = next(iter(real[k]))
        mapping[d] = k
    out_val = 0
    for digit in output:
        real_digit = set(mapping[d] for d in digit)
        found = None
        for val, pat in decimals.items():
            if real_digit == pat:
                found = val
                break
        assert found is not None
        out_val *= 10
        out_val += found
    out += out_val
print(out)
