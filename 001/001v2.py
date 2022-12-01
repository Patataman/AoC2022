""" This solution is shit BUT is very fast to code
"""

from collections import Counter

import sys

with open(sys.argv[1]) as fd:
    bag = fd.read()

cals = []
append_cals = cals.append
elf = None

cbag = str(bag).strip().split("\n\n")
for i, c in enumerate(cbag):
    append_cals(Counter({
        i: int(j)
        for i, j in enumerate(c.split("\n"))
    }).total())

cals.sort(reverse=True)
print(cals[0]+cals[1]+cals[2])
