from collections import Counter

import sys

with open(sys.argv[1]) as fd:
    bag = fd.read()

max_cals = -1
elf = None

cbag = str(bag).strip().split("\n\n")
for i, c in enumerate(cbag):
    cals = Counter({
        i: int(j)
        for i, j in enumerate(c.split("\n"))
    }).total()
    if cals > max_cals:
        max_cals = cals
        elf = i

print(max_cals, i)
