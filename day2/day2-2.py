with open('day2-1.txt') as f:
    lines = f.readlines()

hand_values = { 'X': 1, 'Y': 2, 'Z': 3 }

winning_hands = { 'A': 'Y', 'B': 'Z', 'C': 'X' }
drawing_hands = { 'A': 'X', 'B': 'Y', 'C': 'Z' }
losing_hands  = { 'A': 'Z', 'B': 'X', 'C': 'Y' }
total = 0

for line in lines:
    hands = line.strip().split(" ")
    opponent = hands[0]
    mine = hands[1]

    if mine == 'X':
        total = total + hand_values[losing_hands[opponent]]
    elif mine == 'Y':
        total = total + hand_values[drawing_hands[opponent]] + 3
    else:
        total = total + hand_values[winning_hands[opponent]] + 6

print(total)
