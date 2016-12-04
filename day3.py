"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways
and office furniture that makes up this part of Easter Bunny HQ. This must be a
graphic design department; the walls are covered in specifications for
triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but...
5 10 25? Some of these aren't triangles. You can't help but mark the impossible
ones.

In a valid triangle, the sum of any two sides must be larger than the remaining
side. For example, the "triangle" given above is impossible, because 5 + 10 is
not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""

possible = 0
with open("day3.in") as f:
    for line in f:
        sides = list(map(int, line.split()))
        for i in range(3):
            if sides[i] >= sides[(i+1) % 3] + sides[(i+2) % 3]:
                break
        else:
            possible += 1
print(possible)
