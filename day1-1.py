with open('day1-1.txt') as f:
    lines = f.readlines()

print(lines)

highest_count = 0
current_count = 0

for line in lines:
    if line != "\n":
        current_count = current_count + int(line)
    else:
        highest_count = max(current_count, highest_count)
        current_count = 0

print(highest_count)
