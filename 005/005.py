# Crates are moved one at a time
from pprint import pprint as pp
import sys

""" Process this file to dinamically load
the stacks is going to be a pain, so let's hardcode it :)

As an exercise to the reader, I think the solution will
be remove [, ], trim the whitespaces (to have only 1 space
between stacks) and then process it splitting each row by whitespace
"""

stacks_test = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]

stacks_real = [
    ['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
    ['G', 'W', 'M'],
    ['J', 'N', 'H', 'G'],
    ['J', 'R', 'C', 'N', 'W'],
    ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
    ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
    ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
    ['S', 'J', 'N', 'M', 'G', 'C'],
    ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']
]

with open(sys.argv[1]) as fd:
    data = fd.read().replace(
        "move ",""
    ).replace(
        " from ", " "
    ).replace(
        " to ", " "
    ).strip().split("\n")
    if "test" in sys.argv[1]:
        moves = data[5:]
        stacks = stacks_test
    else:
        moves = data[10:]
        stacks = stacks_real

for move in moves:
    how_many, frm, to = move.split(" ")
    for i in range(int(how_many)):
        stacks[int(to)-1].append(stacks[int(frm)-1].pop())


print("".join([stack[-1] for stack in stacks]))
