# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus
# the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

import sys

with open(sys.argv[1]) as fd:
    games = fd.read().strip().split("\n")
    games = [g.split(" ") for g in games]

score = 0

for elf, me in games:
    if me == "X":
        me = "A"
        score += 1
    elif me == "Y":
        me = "B"
        score += 2
    elif me == "Z":
        me = "C"
        score += 3

    # stolen idea from Pol
    outcome = (ord(elf) - ord(me)) % 3
    if outcome == 0:
        score += 3
    elif outcome == 2:
        score += 6

print(score)
