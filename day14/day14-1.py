with open('day14-1-sample.txt') as f:
    lines = f.readlines()

ranges = []
min_j = 999
max_j = 0
min_i = 999
max_i = 0

grid = []
for i in range(600):
    grid.append([])
    for j in range(600):
        grid[i].append('.')

for line in lines:
    line = line.strip().split(' -> ')

    for i in range(len(line) - 1):
        for coords in line[i: i + 2]:
            x, y = coords.split(',')

            max_j = max(int(x), max_j) # for lazy drawing the grid (DEBUG ONLY)
            max_i = max(int(y), max_i) # for lazy drawing the grid (DEBUG ONLY)
            min_j = min(int(x), min_j) # for lazy drawing the grid (DEBUG ONLY)
            min_i = min(int(y), min_i) # for lazy drawing the grid (DEBUG ONLY)
            
        ranges.append(line[i: i + 2])

for path in ranges:
    one = path[0].split(',')
    two = path[1].split(',')

    start_x = min(int(one[0]), int(two[0]))
    start_y = min(int(one[1]), int(two[1]))
    end_x   = max(int(one[0]), int(two[0]))
    end_y   = max(int(one[1]), int(two[1]))

    for i in range(start_y, end_y+1):
        for j in range(start_x, end_x+1):
            ## print("Setting " + str(start_x) + "," + str(start_y))
            grid[i][j] = '#'



def draw(scan):
    for i in range(0, max_i + 1): # i is top to bottom
        print(str(i) + " " + ''.join(scan[i][min_j:max_j + 1])) # draw one line at a time, much faster than 1 character

def can_move_down(grid, x, y):
##    print("CURRENT COORDS : " + str(x) + "," + str(y))
##    print("CURRENT BLOCK : " + grid[x][y])
##    print("NEXT BLOCK DOWN : " + grid[x][y+1])
    if (grid[x+1][y] == '#') or (grid[x+1][y] == 'o'):
        return False
    return True

def can_move_left_down(grid, x, y):
    if (grid[x+1][y-1] == '#') or (grid[x+1][y-1] == 'o'):
        return False
    return True

def can_move_right_down(grid, x, y):
    if (grid[x+1][y+1] == '#') or (grid[x+1][y+1] == 'o'):
        return False
    return True

settled = 0
voiding = False

while not voiding:
    moving = True

    current_i = 0
    current_j = 500

    while moving:
        # print("---")
        # draw(grid) # draw the grid state
        moving = can_move_down(grid, current_i, current_j) or can_move_left_down(grid, current_i, current_j) or can_move_right_down(grid, current_i, current_j)
        if moving:
            if current_i == max_i:
                voiding = True
                break
            
        if can_move_down(grid, current_i, current_j):
            grid[current_i][current_j] = '.' # update the CURRENT block to be air
            current_i = current_i + 1 # fall one block
            grid[current_i][current_j] = 'o' # update the BELOW block to be sand
        elif can_move_left_down(grid, current_i, current_j):
            grid[current_i][current_j] = '.'
            current_i = current_i + 1
            current_j = current_j - 1
            grid[current_i][current_j] = 'o'
        elif can_move_right_down(grid, current_i, current_j):
            grid[current_i][current_j] = '.'
            current_i = current_i + 1
            current_j = current_j + 1
            grid[current_i][current_j] = 'o'
        else:
            settled = settled + 1

print(settled)
# print(ranges)
