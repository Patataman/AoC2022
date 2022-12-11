""" wtf bro
    You count the pixels on the CRT: 40 wide and 6 high

    Cycle   1 -> ######################################## <- Cycle  40
    Cycle  41 -> ######################################## <- Cycle  80
    Cycle  81 -> ######################################## <- Cycle 120
    Cycle 121 -> ######################################## <- Cycle 160
    Cycle 161 -> ######################################## <- Cycle 200
    Cycle 201 -> ######################################## <- Cycle 240
"""
import sys

with open(sys.argv[1]) as fd:
    mips = fd.read().strip().split("\n")

# Good old 1-D arrays to represent a 2-D array :(
WIDTH = 40
pixel_pos = 1
x, y = 0, 0
cycle = 0

screen = [
    [],
    [],
    [],
    [],
    [],
    [],
]

""" The drawing function only move forwards
which means that if the sprite goes back to a position already painted
nothing will change in the already drawn pixel
"""
def update_cycle(cycle: int) -> (int, int, int):
    """ update cycle and return new values for cycle, x & y
    """
    global WIDTH

    # didnt remember how to do this
    # https://softwareengineering.stackexchange.com/a/212813
    x = cycle % WIDTH;
    y = cycle // WIDTH;

    # cycle represents where the X is at that moment
    cycle += 1

    return cycle, x, y


for order in mips:
    cycle, x, y = update_cycle(cycle)

    valid_positions = [(WIDTH*y)+pixel_pos-1, (WIDTH*y)+pixel_pos, (WIDTH*y)+pixel_pos+1]

    # start drawing the pixel IF the sprite is there
    if cycle-1 in valid_positions:
        # need x-1 because in AoC they start counting on 1
        screen[y].append("#")
    else:
        screen[y].append(".")

    if "addx" in order:
        cycle, x, y = update_cycle(cycle)
        # same as before, only draw IF sprite is on the next pixel to draw
        if cycle-1 in valid_positions:
            screen[y].append("#")
        else:
            screen[y].append(".")

        value = int(order.split(" ")[1])
        pixel_pos += value

# What is the sum of these six signal strengths?
if "test" in sys.argv[1]:
    result = [
        ["##..##..##..##..##..##..##..##..##..##.."],
        ["###...###...###...###...###...###...###."],
        ["####....####....####....####....####...."],
        ["#####.....#####.....#####.....#####....."],
        ["######......######......######......####"],
        ["#######.......#######.......#######....."]
    ]
    for screen_line, res_line in zip(screen, result):
        print("".join(screen_line), res_line)
else:
    for line in screen:
        print("".join(line))

# THIS SOLUTION IS WRONG, BUT LOOKING AT THE TEST RESULT AND THE REAL RESULT YOU
# CAN INFERE THE REAL SOLUTION XDDDDD
