with open('stacks-sample.txt') as f:
    lines = f.readlines()

# stacks = [
#     ["Z", "N"],    # Stack 1
#     ["M", "C", "D"],    # Stack 2
#     ["P"]    # Stack 3
# ]


n = 4
temp_stacks = []
stacks = []
for line in lines[:3]:
    line = [line[i:i+n].strip().replace("[", "").replace("]", "") for i in range(0, len(line), n)]
    temp_stacks.append(line)

transposed_array = zip(*temp_stacks)
for st in list(transposed_array):
    temp = list(st)
    while("" in temp):
        temp.remove("")
    temp.reverse()
    stacks.append(temp)
