with open('day9-1.txt') as f:
    lines = f.readlines()

tail_positions = set()
knot_positions = list()

knot_count = 10
for i in range(knot_count):
  knot_positions.append((0,0))

for move in lines:
  direction = move[0]
  steps = int(move[2:])

  for x in range(steps):
    if direction == 'R':
      knot_positions[0] = (knot_positions[0][0] + 1, knot_positions[0][1])
    elif direction == 'L':
      knot_positions[0] = (knot_positions[0][0] - 1, knot_positions[0][1])
    elif direction == 'U':
      knot_positions[0] = (knot_positions[0][0], knot_positions[0][1] + 1)
    elif direction == 'D':
      knot_positions[0] = (knot_positions[0][0], knot_positions[0][1] - 1)

    for i in range(1, len(knot_positions)):
      # head is top right of tail
      if (knot_positions[i-1][0] > knot_positions[i][0] and knot_positions[i-1][1] > knot_positions[i][1]+1) or (knot_positions[i-1][0] > knot_positions[i][0] + 1 and knot_positions[i-1][1] > knot_positions[i][1]):
        knot_positions[i] = (knot_positions[i][0] + 1, knot_positions[i][1] + 1)

      # head is down right of tail
      elif (knot_positions[i-1][0] > knot_positions[i][0] and knot_positions[i-1][1] < knot_positions[i][1]-1) or  (knot_positions[i-1][0] > knot_positions[i][0] + 1 and knot_positions[i-1][1] < knot_positions[i][1]):
        knot_positions[i] = (knot_positions[i][0] + 1, knot_positions[i][1] - 1)

      # head is up left of tail
      elif (knot_positions[i-1][0] < knot_positions[i][0] and knot_positions[i-1][1] > knot_positions[i][1]+1) or (knot_positions[i-1][0] < knot_positions[i][0] - 1 and knot_positions[i-1][1] > knot_positions[i][1]):
        knot_positions[i] = (knot_positions[i][0] - 1, knot_positions[i][1] + 1)

      # head is down left of tail
      elif (knot_positions[i-1][0] < knot_positions[i][0] and knot_positions[i-1][1] < knot_positions[i][1]-1) or (knot_positions[i-1][0] < knot_positions[i][0] - 1 and knot_positions[i-1][1] < knot_positions[i][1]):
        knot_positions[i] = (knot_positions[i][0] - 1, knot_positions[i][1] - 1)

      # if its more than 1 step right, move tail right
      elif knot_positions[i-1][0] > knot_positions[i][0]+1:
        knot_positions[i] = (knot_positions[i][0] + 1, knot_positions[i][1])
      # if its more than 1 step left, move tail left
      elif knot_positions[i-1][0] < knot_positions[i][0]-1:
        knot_positions[i] = (knot_positions[i][0] - 1, knot_positions[i][1])
      # if its more than 1 step up, move up
      elif knot_positions[i-1][1] > knot_positions[i][1]+1:
        knot_positions[i] = (knot_positions[i][0], knot_positions[i][1] + 1)
      # if its more  than  1 step down, move down
      elif knot_positions[i-1][1] < knot_positions[i][1]-1:
        knot_positions[i] = (knot_positions[i][0], knot_positions[i][1] - 1)

      tail_positions.add(knot_positions[-1])

print(len(tail_positions))