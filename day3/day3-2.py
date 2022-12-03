with open('day3-1.txt') as f:
    lines = f.readlines()

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = {}

for x in range(1, len(characters)+1):
    priorities[characters[x-1]] = x

total = 0

groupings = [lines[x:x+3] for x in range(0, len(lines),3)]

for group in groupings:
    common = ''.join(set.intersection(*map(set,[rucksack.strip() for rucksack in group])))
    total = total + priorities[common]

print(total)

