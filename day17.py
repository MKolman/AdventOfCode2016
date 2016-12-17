from collections import deque
from hashlib import md5

PART1 = False
passcode = "veumntbg"

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
dirnames = "UDLR"

longest_path = 0

q = deque([(0, 0, "")])
while len(q):
    x, y, p = q.popleft()
    if x == y == 3:
        if PART1:
            print(p)
            break
        else:
            longest_path = max(longest_path, len(p))
            continue
    m = md5()
    m.update((passcode+p).encode())
    h = m.hexdigest()

    for n, (i, j) in enumerate(directions):
        if h[n] >= 'b' and 0 <= x+i <= 3 and 0 <= y+j <= 3:
            q.append((x+i, y+j, p+dirnames[n]))

if not PART1:
    print(longest_path)
