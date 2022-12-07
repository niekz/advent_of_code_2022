from collections import defaultdict

with open('day7-1.txt') as f:
    lines = f.readlines()

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirectories = []

    def add_file(self, file):
        self.files.append(file)

    def add_subdirectory(self, subdirectory):
        self.subdirectories.append(subdirectory)

    def calculate_total_size(self):
        total_size = 0
        for file in self.files:
            total_size += file.size

        for subdirectory in self.subdirectories:
            total_size += subdirectory.calculate_total_size()

        return total_size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def pairwise(it):
    it = iter(it)
    while True:
        try:
            yield next(it), next(it)
        except StopIteration:
            return

directories = defaultdict(Directory)

root = Directory('/')
directories['/'] = root

current_directory = root

blocks = ''.join(lines).split("$ ")

for stuff in blocks[1:]: 
    full_stuff = stuff.split()
    command = full_stuff[0]
    args = full_stuff[1:]

    if command == 'ls':
        for a, b in pairwise(args):
            if a == 'dir':
                subdirectory = Directory(current_directory.name + '/' + b)
                current_directory.add_subdirectory(subdirectory)
                directories[subdirectory.name] = subdirectory
            else:
                current_directory.add_file(File(b, int(a)))

    if command == 'cd':
        if args[0] == '/':
            current_directory = root
        elif args[0] == '..':
            current_directory = directories[current_directory.name[:current_directory.name.rfind('/')]]
        else:
            current_directory = directories[current_directory.name + '/' + args[0]]

total_size = root.calculate_total_size()

list_of_subs = [root]

for x in root.subdirectories:
    list_of_subs.append(x)

# WARNING - THIS FUNCTION HAS SIDE EFFECTS
def recurse_tree_and_add_under_100000(subs, total = 0):
    current_node = subs.pop()

    for x in current_node.subdirectories:
        subs.append(x)
    value = 0
    if current_node.name == "/":
        return total
    if current_node.calculate_total_size() <= 100000:
        value = current_node.calculate_total_size()
        return recurse_tree_and_add_under_100000(subs, total + value)
    else:
        return recurse_tree_and_add_under_100000(subs, total)

print(recurse_tree_and_add_under_100000(list_of_subs))
