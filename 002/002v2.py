# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus
# the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

import sys

with open(sys.argv[1]) as fd:
    games = fd.read().strip().split("\n")
    games = [g.split(" ") for g in games]

score = 0
plays = ["A", "B", "C"]
points = {"A": 1, "B": 2, "C": 3}

import pdb; pdb.set_trace()
for elf, res in games:
    if res == "X":
        # Need to lose, so -1 in the array of plays
        score += points[plays[(plays.index(elf)-1)]]  # point for the play
        score += 0  # game result
    elif res == "Y":
        # Need to draw, so same play as the elf
        score += points[elf]  # point for the play
        score += 3
    elif res == "Z":
        # Need to win, so +1 in the array of plays
        score += points[plays[(plays.index(elf)+1) % 3]]  # point for the play
        score += 6

print(score)
