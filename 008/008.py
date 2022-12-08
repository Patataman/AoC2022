import sys

def evaluate_column(grid, tree_x, tree_y):
    # top
    if all([int(grid[tree_y][tree_x]) > int(grid[y][tree_x]) for y in range(0, tree_y)]):
        return True
    # bottom
    if all([int(grid[tree_y][tree_x]) > int(grid[y][tree_x]) for y in range(tree_y+1, len(grid))]):
        return True

    return False

def evaluate_row(grid, tree_x, tree_y):
    # left
    if all([int(grid[tree_y][tree_x]) > int(tree) for tree in grid[tree_y][:tree_x]]):
        return True
    # right
    if all([int(grid[tree_y][tree_x]) > int(tree) for tree in grid[tree_y][tree_x+1:]]):
        return True

    return False

grid = []
with open(sys.argv[1]) as fd:
    data = fd.read().strip().split("\n")

# Border always visible, need to remove corners
x, y = len(data[0]), len(data)
visible_trees = x*2 + y*2 - 4

for line_tree in data:
    grid.append(line_tree)

# Evaluate grid
for _y in range(1, y-1):
    for _x in range(1, x-1):
        if evaluate_column(grid, _x, _y) or evaluate_row(grid, _x, _y):
            visible_trees += 1

print(visible_trees)
