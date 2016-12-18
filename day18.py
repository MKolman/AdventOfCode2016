# Solution for http://adventofcode.com/2016/day/18

curr_line = open("day18.in", "r").readline().strip()
result = curr_line.count(".")
curr_line = ".{}.".format(curr_line)
n = 40
if 0:  # Part 2
    n = 400000

for i in range(n-1):
    curr_line = ["." if curr_line[i-1] == curr_line[i+1] else "^"
                 for i in range(1, len(curr_line) - 1)]
    result += curr_line.count(".")
    curr_line = ".{}.".format("".join(curr_line))

print(result)
