"""
--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get
moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly
unbreakable without the right software. However, the information kiosk designers
at Easter Bunny HQ were not expecting to deal with a master cryptographer like
yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number
of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A,
and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""


def letter_shift(l, n):
    a, z = ord("a"), ord("z")
    i = z - a + 1
    x = ord(l) - a
    x = (x + n) % i
    return chr(x + a)


def word_shift(w, n):
    return "".join(map(lambda l: letter_shift(l, n), w))


id_sum = 0
with open("day4.in") as f:
    for line in f:
        letters = sum(map(list, line.split("-")[:-1]), [])
        room, checksum = line.split("-")[-1].split("[")
        checksum = checksum[:-2]
        room = int(room)

        freq = dict()
        for c in letters:
            if c not in freq:
                freq[c] = 0
            freq[c] -= 1
        data = list(zip(freq.values(), freq.keys()))
        data.sort()
        data = list(zip(*data))
        if data[1][:5] == tuple(checksum):
            id_sum += room
            name = []
            for c in line:
                if c == "-":
                    name.append(" ")
                else:
                    name.append(letter_shift(c, room))
            name = "".join(name)
            if "object storage" in name:
                print(name, room)
