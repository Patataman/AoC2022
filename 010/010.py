""" signal strength (cycle number * value of the X register)
    during cycles
"""

import sys

with open(sys.argv[1]) as fd:
    mips = fd.read().strip().split("\n")

X = 1
cycle = 0
strength = 0

for order in mips:
    # wheather is "noop" or "addx" cycle always +1
    cycle += 1

    if cycle in [20, 60, 100, 140, 180, 220]:
        strength += cycle * X
        print(cycle, strength)

    if "addx" in order:
        # when order is "addx" it takes an extra cycle
        cycle += 1
        # update before the end of the cycle
        if cycle in [20, 60, 100, 140, 180, 220]:
            strength += cycle * X

        value = int(order.split(" ")[1])
        X += value

# What is the sum of these six signal strengths?
print(strength)
