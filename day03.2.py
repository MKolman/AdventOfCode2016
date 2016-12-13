"""
--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you
that triangles are specified in groups of three vertically. Each set of three
numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds
digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed
triangles are possible?
"""

possible = 0
all_sides = []
with open("day3.in") as f:
    for line in f:
        all_sides.append(list(map(int, line.split())))

all_sides = list(zip(*all_sides))
all_sides = all_sides[0] + all_sides[1] + all_sides[2]
for idx in range(0, len(all_sides), 3):
    sides = all_sides[idx:idx + 3]
    for i in range(3):
        if sides[i] >= sides[(i+1) % 3] + sides[(i+2) % 3]:
            break
    else:
        possible += 1
print(possible)
