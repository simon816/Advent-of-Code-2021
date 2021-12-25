import itertools

#range_param = (9, 0, -1)
range_param = (1, 10)

for p in itertools.product(range(*range_param), repeat=5):
    found = False
    print(p)
    z = (p[0] + 6)
    z = ((z * 26) + (p[1] + 11))
    z = ((z * 26) + (p[2] + 5))
    z = ((z * 26) + (p[3] + 6))
    z = ((z * 26) + (p[4] + 8))
    r = ((z % 26) + -1)
    if r >= 1 and r <= 9:
        z = z // 26
        orig_z = z
        chosen_r = r
        for w in range(*range_param):
            z = orig_z
            z = ((z * 26) + (w + 9))
            r = ((z % 26) + -16)
            orig_z2 = z
            if r >= 1 and r <= 9:
                chosen_r2 = r
                for p2 in itertools.product(range(*range_param), repeat=5):
                    z = orig_z2
                    z = z // 26
                    r = ((z % 26) + -8)
                    if r >= 1 and r <= 9 and p2[0] == r:
                        z = z // 26
                        z = ((z * 26) + (p2[1] + 13))
                        r = ((z % 26) + -16)
                        if r >= 1 and r <= 9 and p2[2] == r:
                            z = z // 26
                            r = ((z % 26) + -13)
                            if r >= 1 and r <= 9 and p2[3] == r:
                                z = z // 26
                                r = ((z % 26) + -6)
                                if r >= 1 and r <= 9 and p2[4] == r:
                                    z = z // 26
                                    r = ((z % 26) + -6)
                                    print(p, chosen_r, w, chosen_r2, p2, r)
                                    found = True
                                    break
            if found:
                break
    if found:
        break
