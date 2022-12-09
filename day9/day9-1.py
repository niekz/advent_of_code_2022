with open('day9-1.txt') as f:
    lines = f.readlines()

head_pos = (0, 0)
tail_pos = (0, 0)

tail_positions = set()

for move in lines:
  direction = move[0]
  steps = int(move[2:])

  for x in range(steps):
    if direction == 'R':
      head_pos = (head_pos[0] + 1, head_pos[1])
    elif direction == 'L':
      head_pos = (head_pos[0] - 1, head_pos[1])
    elif direction == 'U':
      head_pos = (head_pos[0], head_pos[1] + 1)
    elif direction == 'D':
      head_pos = (head_pos[0], head_pos[1] - 1)

    # head is top right of tail
    if (head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]+1) or (head_pos[0] > tail_pos[0] + 1 and head_pos[1] > tail_pos[1]):
      tail_pos = (tail_pos[0] + 1, tail_pos[1] + 1)

    # head is down right of tail
    elif (head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]-1) or  (head_pos[0] > tail_pos[0] + 1 and head_pos[1] < tail_pos[1]):
      tail_pos = (tail_pos[0] + 1, tail_pos[1] - 1)

    # head is up left of tail
    elif (head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]+1) or (head_pos[0] < tail_pos[0] - 1 and head_pos[1] > tail_pos[1]):
      tail_pos = (tail_pos[0] - 1, tail_pos[1] + 1)

    # head is down left of tail
    elif (head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]-1) or (head_pos[0] < tail_pos[0] - 1 and head_pos[1] < tail_pos[1]):
      tail_pos = (tail_pos[0] - 1, tail_pos[1] - 1)

    # if its more than 1 step right, move tail right
    elif head_pos[0] > tail_pos[0]+1:
      tail_pos = (tail_pos[0] + 1, tail_pos[1])
    # if its more than 1 step left, move tail left
    elif head_pos[0] < tail_pos[0]-1:
      tail_pos = (tail_pos[0] - 1, tail_pos[1])
    # if its more than 1 step up, move up
    elif head_pos[1] > tail_pos[1]+1:
      tail_pos = (tail_pos[0], tail_pos[1] + 1)
    # if its more  than  1 step down, move down
    elif head_pos[1] < tail_pos[1]-1:
      tail_pos = (tail_pos[0], tail_pos[1] - 1)

    tail_positions.add(tail_pos)

print(len(tail_positions))