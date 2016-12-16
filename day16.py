
def checksum(data):
    data = list(data)
    while len(data) % 2 == 0:
        for i in range(0, len(data), 2):
            data[i] = int(data[i] == data[i+1])
        data = data[::2]
    return "".join(map(str, data))


def fill_disk(salt, n):
    seq = list(map(int, salt))
    while len(seq) < n:
        seq = seq + [0] + [int(not x) for x in seq[::-1]]
    return "".join(map(str, seq[:n]))


print("Part 1:", checksum(fill_disk("11110010111001001", 272)))
# 01110011101111011
print("Part 2:", checksum(fill_disk("11110010111001001", 35651584)))
# 11001111011000111
