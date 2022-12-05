with open('day5-1.txt') as f:
    lines = f.readlines()

# TODO: Read in stacks from the file - below is a shortcut method

# Sample stacks
# stacks = [
#     ["Z", "N"],    # Stack 1
#     ["M", "C", "D"],    # Stack 2
#     ["P"]    # Stack 3
# ]

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

def move_n_crates(from_stack, to_stack, n_crates):
  temp_crates = []
  for i in range(n_crates):
    temp_crates.append(from_stack.pop())
  for i in range(n_crates):
    to_stack.append(temp_crates.pop())


def top_crate(stack):
  return stack[-1]


rearrangement = []

# hard coded from where to read re-arrangements.
for line in lines[10:]:
  split = line.strip().split()
  rearrangement.append((int(split[1]), int(split[3]), int(split[5])))

for step in rearrangement:
  num_crates, from_stack, to_stack = step
  move_n_crates(stacks[from_stack - 1], stacks[to_stack - 1], num_crates)

for stack in stacks:
  print(top_crate(stack)),  # The comma is to print on the same line
