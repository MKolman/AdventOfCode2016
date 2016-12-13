from collections import deque

# All elements gen1, mic1, gen2, mic2
pos = (1, 1, 1, 1, 0, 0, 0, 0, 1, 2)  # Part 1
pos = (1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2)  # Part 2: 61 [Finished in 1674.0s]
# Number of floors
nfl = 4
npair = len(pos) // 2

visited = set()
q = deque([(0, 0, list(pos))])
prev = 0
prev3 = 0
while len(q):
    elev, moves, pos = q.popleft()
    if elev < 0 or elev > 3:
        continue
    if moves != prev:
        print(elev, moves, pos, len(q))
        prev = moves
    if prev3 < pos.count(nfl - 1):
        print(elev, moves, pos, len(q))
        prev3 = pos.count(nfl - 1)
    if pos == [nfl - 1] * (2 * npair):
        print(moves)
        break
    if (elev, tuple(pos)) in visited:
        continue
    visited.add((elev, tuple(pos)))

    invalid = False
    for i in range(0, npair * 2, 2):
        if pos[i] != pos[i + 1]:
            for j in range(0, npair * 2, 2):
                if pos[j] == pos[i + 1]:
                    invalid = True
                    break
            if invalid:
                break
    if invalid:
        continue

    for i in range(2 * npair):
        if pos[i] != elev:
            continue
        pos[i] += 1
        if (elev + 1, tuple(pos)) not in visited:
            q.append((elev + 1, moves + 1, pos[:]))
        for j in range(2 * npair):
            if pos[j] != elev:
                continue
            pos[j] += 1
            if (elev + 1, tuple(pos)) not in visited:
                q.append((elev + 1, moves + 1, pos[:]))
            pos[j] -= 1

        pos[i] -= 2
        if (elev - 1, tuple(pos)) not in visited:
            q.append((elev - 1, moves + 1, pos[:]))
        for j in range(2 * npair):
            if pos[j] != elev:
                continue
            pos[j] -= 1
            if (elev - 1, tuple(pos)) not in visited:
                q.append((elev - 1, moves + 1, pos[:]))
            pos[j] += 1
        pos[i] += 1




