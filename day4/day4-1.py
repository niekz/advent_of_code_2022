with open('day4-1.txt') as f:
    lines = f.readlines()

total = 0

for grouping in lines:
  assignments = grouping.strip().split(",")
  
  ass1_ranges = assignments[0].split("-")
  ass2_ranges = assignments[1].split("-")
  
  ass1 = [i for i in range(int(ass1_ranges[0]), int(ass1_ranges[1])+1)]
  ass2 = [i for i in range(int(ass2_ranges[0]), int(ass2_ranges[1])+1)]

  if all(item in ass1 for item in ass2) or all(item in ass2 for item in ass1):
    total = total + 1

print(total)
  
