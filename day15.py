# Solution for
# http://adventofcode.com/2016/day/15

data = [[13, 10], [17, 15], [19, 17], [7, 1], [5, 0], [3, 1]]
if False:  # For part 2
    data.append([11, 0])

for delay in range(3 * 5 * 7 * 11 * 13 * 17 * 19):
    for i in range(len(data)):
        if (data[i][1] + delay + i + 1) % data[i][0] != 0:
            break
    else:
        print(delay)
        break
