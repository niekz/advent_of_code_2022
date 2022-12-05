with open('day5-1.txt') as f:
    lines = f.readlines()

# TODO: Read in stacks from the file - below is a shortcut method

# Sample stacks
# stacks = [
#     ["Z", "N"],    # Stack 1
#     ["M", "C", "D"],    # Stack 2
#     ["P"]    # Stack 3
# ]

stacks = [
  ["D", "B", "J", "V"],
  ["P", "V", "B", "W", "R", "D", "F"],
  ["R", "G", "F", "L", "D", "C", "W", "Q"],
  ["W", "J", "P", "M", "L", "N", "D", "B"],
  ["H", "N", "B", "P", "C", "S", "Q"],
  ["R", "D", "B", "S", "N", "G"],
  ["Z", "B", "P", "M", "Q", "F", "S", "H"],
  ["W", "L", "F"],
  ["S", "V", "F", "M", "R"]
]

# Part 1
def move_crate(from_stack, to_stack):
    to_stack.append(from_stack.pop())

def top_crate(stack):
    return stack[-1]

rearrangement = []

for line in lines[10:]:
  split = line.strip().split()
  rearrangement.append((int(split[1]), int(split[3]), int(split[5])))

for step in rearrangement:
    num_crates, from_stack, to_stack = step

    for i in range(num_crates):
        move_crate(stacks[from_stack - 1], stacks[to_stack - 1])

for stack in stacks:
  print(top_crate(stack)), # The comma is to print on the same line