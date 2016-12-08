"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an
implementation of two-factor authentication after a long game of requirements
telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a
nearby desk). Then, it displays a code on a little screen, and you type that
code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken
everything apart and figured out how it works. Now you just have to work out
what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for
the screen; these instructions are your puzzle input. The screen is 50 pixels
wide and 6 pixels tall, all of which start off, and is capable of three somewhat
peculiar operations:

-rect AxB turns on all of the pixels in a rectangle at the topleft of the screen
which is A wide and B tall.

-rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right
by B pixels. Pixels that would fall off the right end appear at the left end of
the row.

-rotate column x=A by B shifts all of the pixels in column A (0 is the left
column) down by B pixels. Pixels that would fall off the bottom appear at the
top of the column.

For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:
###....
###....
.......

rotate column x=1 by 1 rotates the second column down by one pixel:
#.#....
###....
.#.....

rotate row y=0 by 4 rotates the top row right by four pixels:
....#.#
###....
.#.....

rotate column x=1 by 1 again rotates the second column down by one pixel,
causing the bottom pixel to wrap back to the top:
.#..#.#
#.#....
.#.....

As you can see, this display technology is extremely powerful, and will soon
dominate the tiny-code-displaying-screen market. That's what the advertisement
on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display:
after you swipe your card, if the screen did work, how many pixels should be
lit?
"""


def disp(s):
    print("\n".join(map(lambda x: "".join(x) + "|", s)))

H = 6
screen = [[" "] * 50 for i in range(H)]
disp(screen)
with open("day8.in") as f:
    for line in f:
        # print(line)
        if line.startswith("rect"):
            a, b = map(int, line.split()[1].split("x"))
            for i in range(a):
                for j in range(b):
                    screen[j][i] = "*"
        elif line.startswith("rotate row"):
            row, dist = map(int, line.split("=")[1].split(" by "))
            screen[row] = screen[row][-dist:] + screen[row][:-dist]
        elif line.startswith("rotate column"):
            col, dist = map(int, line.split("=")[1].split(" by "))
            c = [screen[i][col] for i in range(H)]
            for i in range(H):
                screen[i][col] = c[(i - dist) % H]
        # disp(screen)

disp(screen)
c = sum(l.count("*") for l in screen)
print(c)
