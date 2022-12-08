import sys

def evaluate_column(grid, tree_x, tree_y):
    h = grid[tree_y][tree_x]

    # top
    top = 0
    for y in range(tree_y-1, -1, -1):
        top += 1
        if h <= grid[y][tree_x]:
            break
    # bottom
    bottom = 0
    for y in range(tree_y+1, len(grid)):
        bottom += 1
        if h <= grid[y][tree_x]:
            break

    return top * bottom

def evaluate_row(grid, tree_x, tree_y):
    h = grid[tree_y][tree_x]

    # left
    left = 0
    for x in range(tree_x-1, -1, -1):
        left += 1
        if h <= grid[tree_y][x]:
            break
    # right
    right = 0
    for x in range(tree_x+1, len(grid[tree_y])):
        right += 1
        if h <= grid[tree_y][x]:
            break

    return left * right

grid = []
with open(sys.argv[1]) as fd:
    data = fd.read().strip().split("\n")

# Border always visible, need to remove corners
x, y = len(data[0]), len(data)

for line_tree in data:
    grid.append(line_tree)

# Evaluate grid
score = 0
for _y in range(1, y-1):
    for _x in range(1, x-1):
        new_score = evaluate_column(grid, _x, _y) * evaluate_row(grid, _x, _y)
        if new_score > score:
            score = new_score

print(score)
