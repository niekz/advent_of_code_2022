with open('day8-1.txt') as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]
transposed_grid = list(zip(*grid))

def calculate_highest_scenic_score(grid):
    scenic_score = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tree_score = 0

            row = grid[j]
            column = list(transposed_grid[i])

            left = 0
            right = 0
            up = 0
            down = 0

            left_of_current = row[:i]
            left_of_current.reverse()
            right_of_current = row[i+1:]
            up_of_current = column[:j]
            up_of_current.reverse()
            down_of_current = column[j+1:]

            for tree_count in range(len(left_of_current)):
                if grid[j][i] >= left_of_current[tree_count]:
                    left = left + 1
                    if grid[j][i] == left_of_current[tree_count]:
                        break
                elif grid[j][i] < left_of_current[tree_count] and tree_count > 0:
                    left = left + 1
                    break
                else:
                    break

            for tree_count in range(len(right_of_current)):
                if grid[j][i] >= right_of_current[tree_count]:
                    right = right + 1
                    if grid[j][i] == right_of_current[tree_count]:
                        break
                elif grid[j][i] < right_of_current[tree_count] and tree_count > 0:
                    right = right + 1
                    break
                else:
                    break

            for tree_count in range(len(up_of_current)):
                if grid[j][i] >= up_of_current[tree_count]:
                    up = up + 1
                    if grid[j][i] == up_of_current[tree_count]:
                        break
                elif grid[j][i] < up_of_current[tree_count] and tree_count > 0:
                    up = up + 1
                    break
                else:
                    break

            for tree_count in range(len(down_of_current)):
                if grid[j][i] >= down_of_current[tree_count]:
                    down = down + 1
                    if grid[j][i] == down_of_current[tree_count]:
                        break
                elif grid[j][i] < down_of_current[tree_count] and tree_count >= 0:
                    down = down + 1
                    break
                else:
                    break

            tree_score = up * down * left * right
            scenic_score = max(scenic_score, tree_score)
    return scenic_score

print(calculate_highest_scenic_score(grid))