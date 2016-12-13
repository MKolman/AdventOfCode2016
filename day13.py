from collections import deque

PART = 2

INPUT = 1350
def is_wall(x, y):
    n = x*x + 3*x + 2*x*y + y + y*y + INPUT
    return bin(n).count('1') % 2

visited = set()
q = deque([(0, 1, 1)])
while len(q):
    steps, x, y = q.popleft()
    if PART == 1:
        if (x, y) == (31, 39):
            print(steps)
            break
    else:
        if steps > 50:
            break
    if (x,y) in visited:
        continue
    visited.add((x, y))

    for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if x+i < 0 or y+j < 0:
            continue
        if not is_wall(x+i, y+j):
            q.append((steps+1, x+i, y+j))

if PART == 2:
    print(len(visited))
