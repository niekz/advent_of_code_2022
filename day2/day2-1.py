with open('day2-1.txt') as f:
    lines = f.readlines()

hand_values = { 'X': 1, 'Y': 2, 'Z': 3 }

winning_hands = { 'A': 'Y', 'B': 'Z', 'C': 'X' }
drawing_hands = { 'A': 'X', 'B': 'Y', 'C': 'Z' }


total = 0

for line in lines:
    hands = line.strip().split(" ")
    opponent = hands[0]
    mine = hands[1]

    if winning_hands[opponent] == mine:
        total = total + hand_values[mine] + 6
    elif drawing_hands[opponent] == mine:
        total = total + hand_values[mine] + 3
    else:
        total = total + hand_values[mine]


print(total)
