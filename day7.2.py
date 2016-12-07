"""
--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the
supernet sequences (outside any square bracketed sections), and a corresponding
Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any
three-character sequence which consists of the same character twice with a
different character between them, such as xyx or aba. A corresponding BAB is the
same characters but in reversed positions: yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab
within square brackets).

xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).

aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet;
the aaa sequence is not related, because the interior character must be
different).

zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a
corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?
"""

correct = 0
with open("day7.in") as f:
    for line in f:
        br = False
        foundout = set()
        foundin = set()
        for i, c in enumerate(line[:-2]):
            if c == "[":
                br = True
                continue
            if c == "]":
                br = False
                continue
            if c == line[i + 2] and c != line[i + 1]:
                if br:
                    foundin.add((line[i + 1], c))
                else:
                    foundout.add((c, line[i + 1]))
        if (foundin & foundout):
            correct += 1


print(correct)
