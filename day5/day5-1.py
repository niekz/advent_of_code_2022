with open('day5-1.txt') as f:
    lines = f.readlines()

n = 4
temp_stacks = []
stacks = []
for line in lines[:8]:
    line = [line[i:i+n].strip().replace("[", "").replace("]", "") for i in range(0, len(line), n)]
    temp_stacks.append(line)

transposed_array = zip(*temp_stacks)
for st in list(transposed_array):
    temp = list(st)
    while("" in temp):
        temp.remove("")
    temp.reverse()
    stacks.append(temp)

def move_crate(from_stack, to_stack):
    to_stack.append(from_stack.pop())


def top_crate(stack):
    return stack[-1]


rearrangement = []

# hard coded from where to read re-arrangements.
for line in lines[10:]:
  split = line.strip().split()
  rearrangement.append((int(split[1]), int(split[3]), int(split[5])))

for step in rearrangement:
    num_crates, from_stack, to_stack = step

    for i in range(num_crates):
        move_crate(stacks[from_stack - 1], stacks[to_stack - 1])

for stack in stacks:
  print(top_crate(stack)),  # The comma is to print on the same line
