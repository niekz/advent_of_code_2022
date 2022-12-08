with open('day8-1.txt') as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]
transposed_grid = list(zip(*grid))

def count_visible_trees(grid):
    visible_trees = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            row = grid[j]
            column = transposed_grid[i]

            if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[i])-1:
                visible_trees = visible_trees + 1
                continue

            if grid[j][i] > max(row[:i], key=int) or grid[j][i] > max(row[i+1:], key=int):
                visible_trees = visible_trees + 1
                continue

            if grid[j][i] > max(column[:j], key=int) or grid[j][i] > max(column[j+1:], key=int):
                visible_trees = visible_trees + 1
                continue

    return visible_trees

print(count_visible_trees(grid)) 