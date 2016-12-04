def num(p):
    if p.imag == 2:
        return 1
    if p.imag == 1:
        return int(p.real + 3)
    if p.imag == 0:
        return int(p.real + 7)
    if p.imag == -1:
        return chr(ord("A") + int(p.real + 1))
    return "D"


def is_valid(p):
    return abs(p.real) + abs(p.imag) <= 2



f = open("day2.txt", "r")
dat = f.read()
f.close()
# dat = """ULL
# RRDDD
# LURDL
# UUUUD"""
pos = -2
d = dict(R=1,L=-1,U=1j,D=-1j)

for l in dat:
    if l == "\n":
        print(num(pos))
        continue
    pos += d[l]
    if not is_valid(pos):
        pos -= d[l]
    # print(l, num(pos))
