"""
--- Part Two ---

Of course, that would be the message - if you hadn't agreed to use a modified
repetition code instead.

In this modified code, the sender instead transmits what looks like random data,
but for each character, the character they actually want to send is slightly
less likely than the others. Even after signal-jamming noise, you can look at
the letter distributions in each column and choose the least common letter to
reconstruct the original message.

In the above example, the least common character in the first column is a; in
the second, d, and so on. Repeating this process for the remaining characters
produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what
is the original message that Santa is trying to send?
"""

data = []
with open("day6.in") as f:
    for line in f:
        data.append(list(line.strip()))

word = ""
for line in zip(*data):
    m = (float("inf"), "0")
    for c in line:
        m = min(m, (line.count(c), c))
    word = word + m[1]
print(word)
