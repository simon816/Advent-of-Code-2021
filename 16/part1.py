import sys

packet_hex = sys.stdin.readline()

packet = []
for n in packet_hex.strip():
    packet.extend(map(int, '%04d' % int(bin(int(n, 16))[2:])))

def num(bits):
    return int(''.join(map(str,bits)), 2)

version_sum = 0

def parse(stream, pos):
    global version_sum
    version = num(stream[pos:pos + 3])
    type_id = num(stream[pos + 3:pos + 6])
    pos += 6
    version_sum += version
    if type_id == 4:
        pos, val = parse_lit(stream, pos)
    else:
        length_type = stream[pos]
        if length_type == 0:
            bit_len = num(stream[pos + 1:pos + 16])
            pos += 16
            read = 0
            while read != bit_len:
                new_pos = parse(stream, pos)
                read += new_pos - pos
                pos = new_pos
        else:
            sub_num = num(stream[pos + 1:pos + 12])
            pos += 12
            for _ in range(sub_num):
                pos = parse(stream, pos)
    return pos


def parse_lit(stream, pos):
    lit_bits = []
    while True:
        val = stream[pos:pos + 5]
        lit_bits.extend(val[1:])
        pos += 5
        if val[0] == 0:
            break
    return pos, num(lit_bits)

pos = parse(packet, 0)
assert sum(packet[pos:]) == 0

print(version_sum)
