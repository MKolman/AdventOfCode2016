# A solution for Part 1 and Part 2 of
# http://adventofcode.com/2016/day/14

from hashlib import md5
from bisect import bisect_left

nhash = 1  # Part 1
nhash = 2017  # Part 2

# Get all the hex characters
ch = [hex(i)[-1] for i in range(16)]
# All indexes with 3 characters repeated
tri = {c: [] for c in ch}
# The final keys
keys = set()
# The input
salt = "qzyelonm"
# salt = "abc"  # test

i = 0
while len(keys) < 100:
    # 1. Do the hashing
    k = salt + str(i)
    for j in range(nhash):
        m = md5()
        m.update(k.encode())
        k = m.hexdigest()

    # 2. Look if there are 3 reapeated character in the hash
    for j in range(len(k) - 2):
        if k[j] == k[j + 1] == k[j + 2]:
            tri[k[j]].append(i)
            break

    # 3. Look if there are 5 repeated characters in the hash
    for c in ch:
        if c * 5 in k:
            # 3.1 If there are: find all the hashes in the past 1000 that have
            # the same character repeated 3 times and save them
            idx = bisect_left(tri[c], i - 1000)
            while idx < len(tri[c]) and tri[c][idx] < i:
                keys.add(tri[c][idx])
                # print(len(keys))
                idx += 1
    i += 1

print(sorted(keys)[63])
