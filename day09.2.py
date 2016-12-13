"""--- Day 9: Explosives in Cyberspace ---

Wandering around a secure area, you come across a datalink port to a new part of
the network. After briefly scanning it for interesting files, you find one file
in particular that catches your attention. It's compressed with an experimental
format, but fortunately, the documentation for the format is nearby.

The format compresses a sequence of characters. Whitespace is ignored. To
indicate that some sequence should be repeated, a marker is added to the file,
like (10x2). To decompress this marker, take the subsequent 10 characters and
repeat them 2 times. Then, continue reading the file after the repeated data.
The marker itself is not included in the decompressed output.

If parentheses or other characters appear within the data referenced by a
marker, that's okay - treat it like normal data, not a marker, and then resume
looking for markers after the decompressed section.

For example:

ADVENT contains no markers and decompresses to itself with no changes, resulting
in a decompressed length of 6.

A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a
decompressed length of 7.

(3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.

A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed
length of 11.

(6x1)1x3)A simply becomes 1x3)A - the 1x3) looks like a marker, but because it's
(within a data section of another marker, it is not treated any differently from
(the A that comes after it. It has a decompressed length of 6.

X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18),
because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped
and not processed further.

What is the decompressed length of the file (your puzzle input)? Don't count
whitespace.
"""
import sys
sys.setrecursionlimit(10000)

def ln(txt):
    """ ln(s(bxa)t) = |s| + q + (a-1) ln(t[q:b]+t[:q]) + ln(t[q:])
    q := """
    tmp = txt.split('(', 1)

    if len(tmp) == 1:  # No (axb)
        return len(txt)

    s, t = tmp
    b, a = map(int, t.split(')', 1)[0].split("x"))
    t = txt.split(')', 1)[1]
    q = t.index('(') if '(' in t else len(t)
    return len(s) + q + (a - 1) * ln(t[q:b] + t[:q]) + ln(t[q:])




with open("day9.in") as f:
    for txt in f:
        print(ln(txt.strip()))
