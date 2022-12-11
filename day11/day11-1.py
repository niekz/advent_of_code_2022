with open('day11-1.txt') as f:
    lines = f.readlines()

# Parse input
monkeys = []
for line in lines:
  line = line.strip()
  if line.startswith('Monkey'):
    monkeys.append({
      'items': [],
      'operation': None,
      'value1': None,
      'inspected': 0,
      'test': None,
      'if_true': None,
      'if_false': None,
    })
    continue
  if line.startswith('Starting items:'):
    monkeys[-1]['items'] = [int(item.replace(",", "")) for item in line.split()[2:]]
  elif line.startswith('Operation:'):
    monkeys[-1]['operation'] = line.split()[4]
    monkeys[-1]['value1'] = line.split()[5]
  elif line.startswith('Test:'):
    monkeys[-1]['test'] = line.split()[3]
  elif line.startswith('If true:'):
    monkeys[-1]['if_true'] = line.split()[5]
  elif line.startswith('If false:'):
    monkeys[-1]['if_false'] = line.split()[5]

for rounds in range(20):
  monkey_count = 0
  # Evaluate operations
  for monkey in monkeys:
    print("Monkey " + str(monkey_count))
    monkey_count = monkey_count + 1
    for i in range(len(monkey['items'])):
      monkey['inspected'] = monkey['inspected'] + 1
      item = monkey['items'][i]
      print(" Monkey inspects an item with a worry level of " + str(item) + ".")
      value1 = monkey['value1']
      if value1 == 'old':
        value1 = item

      print("   Worry level changed by OP " + monkey['operation'] + " to " + str(eval(str(item) + monkey['operation'] + str(value1))))
      monkey['items'][i] = eval(str(item) + monkey['operation'] + str(value1)) # eval the operation
      monkey['items'][i] //= 3 # divide by 3
      print("   Monkey gets bored with item. Worry level is divided by 3 to " + str(monkey['items'][i]))
      if eval(str(monkey['items'][i]) + "%" + monkey['test']) == 0:
        print("   Current worry level is not divisible by " + str(monkey['test']))
        monkeys[int(monkey['if_true'])]['items'].append(monkey['items'][i])
        # print(monkeys[int(monkey['if_true'])]['items'])
        print("   Item with worry level " + str(monkey['items'][i]) + " is thrown to monkey " + monkey['if_true'] + ".")
      else:
        print("   Current worry level is not divisible by " + str(monkey['test']))
        monkeys[int(monkey['if_false'])]['items'].append(monkey['items'][i])
        print("   Item with worry level " + str(monkey['items'][i]) + " is thrown to monkey " + monkey['if_false'] + ".")

    monkey['items'] = []

  print()

  # Print items held by each monkey
  for i, monkey in enumerate(monkeys):
    print('Monkey {}: {}'.format(i, monkey['items']))

# Print items held by each monkey
  for i, monkey in enumerate(monkeys):
    print('Monkey {}: {}'.format(i, monkey['inspected']))

most_active = sorted([monkey['inspected'] for monkey in monkeys])[-2:]
print(most_active[0] * most_active[1])