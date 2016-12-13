"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course,
the list is encrypted and full of decoy data, but the instructions to decode the
list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in
the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a
(5), b (3), and then a tie between x, y, and z, which are listed alphabetically.

a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all
tied (1 of each), the first five are listed alphabetically.

not-a-real-room-404[oarel] is a real room.

totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""

id_sum = 0
with open("day4.in") as f:
    for line in f:
        letters = sum(map(list, line.split("-")[:-1]), [])
        room, checksum = line.split("-")[-1].split("[")
        checksum = checksum[:-2]

        freq = dict()
        for c in letters:
            if c not in freq:
                freq[c] = 0
            freq[c] -= 1
        data = list(zip(freq.values(), freq.keys()))
        data.sort()
        data = list(zip(*data))
        # print(data[:5], checksum)
        if data[1][:5] == tuple(checksum):
            id_sum += int(room)
        # break

print(id_sum)
