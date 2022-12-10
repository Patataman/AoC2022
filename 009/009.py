from collections import defaultdict
import sys

# X, Y
HEAD = [0,0]
TAIL = [0,0]

UNIQUE_POSITIONS = defaultdict()
UNIQUE_POSITIONS[str(TAIL)] = None

with open(sys.argv[1]) as fd:
    moves = fd.read().strip().split("\n")

def move_tail():
    """ Moves the tail """
    global HEAD, TAIL, UNIQUE_POSITIONS
    # Euclidean distance
    dist_head = ((HEAD[0] - TAIL[0])**2 + (HEAD[1] - TAIL[1])**2)**(1/2)
    move_h = HEAD[0] - TAIL[0]
    move_v = HEAD[1] - TAIL[1]
#     if HEAD[0] == 4 and HEAD[1] == 2:
#         import pdb; pdb.set_trace()

    if dist_head == 2:
        # dist == 2, only 1 direction
        # Might move horizontally
        if move_h != 0:
            TAIL[0] += 1 if move_h > 0 else -1
        # Might move vertically
        if move_v != 0:
            TAIL[1] += 1 if move_v > 0 else -1
    elif dist_head > 2:
        # dist > 2, both directions
        # move horizontally, max 1 block
        TAIL[0] += 1 if move_h > 0 else -1
        # move vertically, max 1 block
        TAIL[1] += 1 if move_v > 0 else -1

    # register new position as visited
    UNIQUE_POSITIONS[str(TAIL)] = None

def move_head(steps, axis):
    """ Moves the head """
    for s in range(steps):
        # switch because yes
        if axis == "r":
            HEAD[0] += 1
        elif axis == "l":
            HEAD[0] -= 1
        elif axis == "u":
            HEAD[1] += 1
        elif axis == "d":
            HEAD[1] -= 1
        else:
            pass

        # Update tail position if needed
        move_tail()


for text in moves:
    axis, steps = text.split(" ")
    move_head(int(steps), axis.lower())

print("HEAD", HEAD, "TAIL", TAIL)
print("Visited", len(UNIQUE_POSITIONS.keys()))
