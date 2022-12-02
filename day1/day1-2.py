with open('day1-1.txt') as f:
    lines = f.readlines()

lines.append("\n")

def max_3(count_list):
    return sorted(count_list, reverse=True)[:3]

highest_count = [0,0,0]
current_count = 0

for line in lines:
    if line != "\n":
        current_count = current_count + int(line)
    else:
        highest_count.append(current_count)
        highest_count = max_3(highest_count)
        current_count = 0

print(sum(highest_count))

