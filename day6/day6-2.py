with open('day6-1.txt') as f:
    lines = f.readlines()

seq = [character for character in lines[0]]
window_size = 14

for i in range(len(seq) - window_size + 1):
    currentSeq = seq[i: i + window_size]
    if len(currentSeq) == len(set(currentSeq)):
        print("First unique indicator: " + str(i+window_size))
        break
