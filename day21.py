from itertools import permutations

lines = open("day21.in", "r").readlines()


def scramble(password):
    password = list(password)
    for line in lines:
        if line.startswith("swap position"):
            line = line.split()
            a, b = int(line[2]), int(line[5])
            password[a], password[b] = password[b], password[a]
        elif line.startswith("swap letter"):
            line = line.split()
            a, b = password.index(line[2]), password.index(line[5])
            password[a], password[b] = password[b], password[a]
        elif line.startswith("move"):
            line = line.split()
            a, b = int(line[2]), int(line[5])
            x = password.pop(a)
            password.insert(b, x)
        elif line.startswith("rotate based"):
            line = line.split()
            n = password.index(line[6]) + 1
            n += n >= 5
            n %= len(password)
            password = password[-n:] + password[:-n]
        elif line.startswith("rotate"):
            line = line.split()
            n = int(line[2])
            if line[1] == "right":
                password = password[-n:] + password[:-n]
            else:
                password = password[n:] + password[:n]
        elif line.startswith("reverse"):
            line = line.split()
            a, b = sorted([int(line[2]), int(line[4])])
            password[a:b+1] = password[a:b+1:][::-1]
        else:
            assert 0, "Weird line"
    return "".join(password)


password = "abcdefgh"
part1 = scramble(password)  # bfheacgd
print("Part 1:", part1)

clue = "fbgdceah"

for p in permutations("abcdefgh"):
    if scramble(p) == clue:
        print("Part 2:", "".join(p))
        break
