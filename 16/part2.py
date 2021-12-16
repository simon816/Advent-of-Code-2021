import sys
import functools

packet_hex = sys.stdin.readline()

packet = []
for n in packet_hex.strip():
    packet.extend(map(int, '%04d' % int(bin(int(n, 16))[2:])))

def num(bits):
    return int(''.join(map(str,bits)), 2)


def parse(stream, pos):
    version = num(stream[pos:pos + 3])
    type_id = num(stream[pos + 3:pos + 6])
    pos += 6
    if type_id == 4:
        pos, val = parse_lit(stream, pos)
    else:
        sub_vals = []
        length_type = stream[pos]
        if length_type == 0:
            bit_len = num(stream[pos + 1:pos + 16])
            pos += 16
            read = 0
            while read != bit_len:
                new_pos, sub_val = parse(stream, pos)
                sub_vals.append(sub_val)
                read += new_pos - pos
                pos = new_pos
        else:
            sub_num = num(stream[pos + 1:pos + 12])
            pos += 12
            for _ in range(sub_num):
                pos, sub_val = parse(stream, pos)
                sub_vals.append(sub_val)
        if type_id == 0:
            val = sum(sub_vals)
        elif type_id == 1:
            val = functools.reduce(lambda a,b:a*b, sub_vals,1)
        elif type_id == 2:
            val = min(sub_vals)
        elif type_id == 3:
            val = max(sub_vals)
        elif type_id == 5:
            val = 1 if sub_vals[0] > sub_vals[1] else 0
        elif type_id == 6:
            val = 1 if sub_vals[0] < sub_vals[1] else 0
        elif type_id == 7:
            val = 1 if sub_vals[0] == sub_vals[1] else 0
    return pos, val


def parse_lit(stream, pos):
    lit_bits = []
    while True:
        val = stream[pos:pos + 5]
        lit_bits.extend(val[1:])
        pos += 5
        if val[0] == 0:
            break
    return pos, num(lit_bits)

pos, val = parse(packet, 0)
assert sum(packet[pos:]) == 0

print(val)
