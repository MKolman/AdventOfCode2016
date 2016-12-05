"""
--- Part Two ---

As the door slides open, you are presented with a second door that uses a
slightly more inspired security mechanism. Clearly unimpressed by the last
version (in what movie is the password decrypted in order?!), the Easter Bunny
engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also
indicates the position within the password to fill. You still look for hashes
that begin with five zeroes; however, now, the sixth character represents the
position (0-7), and the seventh character is the character to put in that
position.

A hash result of 000001f means that f is the second character in the password.
Use only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:

The first interesting hash is from abc3231929, which produces 0000015...; so, 5
goes in position 1: _5______.

In the previous method, 5017308 produced an interesting hash; however, it is
ignored, because it specifies an invalid position (8).

The second interesting hash is at index 5357525, which produces 000004e...; so,
e goes in position 4: _5__e___.

You almost choke on your popcorn as the final character falls into place,
producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password? Be extra
proud of your solution if it uses a cinematic "decrypting" animation.

Your puzzle input is still ffykfhsq.
"""

from hashlib import md5


def is_valid(door, n):
    coder = md5()
    coder.update(("{}{}".format(door, n)).encode())
    code = coder.hexdigest()
    return (code[5], code[6]) if code.startswith("00000") else (False, False)


door = "ffykfhsq"
password = ["-1" for i in range(8)]
for i in range(100000000):
    pos, code = is_valid(door, i)
    if code is not False:
        if "0" <= pos <= "7" and password[int(pos)] == "-1":
            password[int(pos)] = code
            print(i, pos, code, "".join(password))
    if "-1" not in password:
        break

# 8c35d1ab
print("".join(password))
