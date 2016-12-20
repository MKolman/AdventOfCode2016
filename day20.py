# Solution for http://adventofcode.com/2016/day/20

# First read al the blacklist rules
rules = []
with open("day20.in") as f:
    for i, line in enumerate(f):
        start, end = map(int, line.split("-"))
        rules.append((start, end))

# Sort the rules by starting IP
rules.sort()
new_rules = [0, 0]  # A cumulative rule start-end
num_allowed = 0
for start, end in rules:
    if start <= new_rules[1] + 1:
        # If we have overlapping rules just extend them
        new_rules[1] = max(new_rules[1], end)
    else:
        # If we have a gap in the rules mark it and move on
        if new_rules[0] == 0:
            print("Part 1:", new_rules[1] + 1)  # 23923783
        num_allowed += start - new_rules[1] - 1
        new_rules = [start, end]

print("Part 2:", num_allowed)  # 125
