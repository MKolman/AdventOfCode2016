# Solution for http://adventofcode.com/2016/day/19
from math import log, floor, ceil


# Part 1
def part1(n):
    k = floor(log(n) / log(2))
    return 2*(n - 2**k) + 1


# Part 2
def part2(n):
    k = ceil(log(n) / log(3))
    res = n - 3**(k-1)
    if res > 3**(k-1):
        res += res - 3**(k-1)
    return res


n = 3014387
print("Part 1", part1(n))  # 1834471
print("Part 2", part2(n))  # 1420064
