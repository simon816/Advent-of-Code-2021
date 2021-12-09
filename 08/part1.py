import sys

count = 0

for line in sys.stdin.readlines():
    patterns, output = line.strip().split('|')
    patterns = patterns.strip().split(' ')
    output = output.strip().split(' ')
    for digit in output:
        if len(digit) in [2, 3, 7, 4]:
            count += 1

print(count)
