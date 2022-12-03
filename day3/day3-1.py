with open('day3-1.txt') as f:
    lines = f.readlines()

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = {}

for x in range(1, len(characters)+1):
    priorities[characters[x-1]] = x

total = 0

for rucksack in lines:
    first_ruck  = rucksack[:len(rucksack)//2]
    second_ruck = rucksack[len(rucksack)//2:]

    common_character = ''.join(set(first_ruck).intersection(second_ruck))

    total = total + priorities[common_character]

print(total)

