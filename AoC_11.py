import math
from collections import deque

input = open('input_11', 'r')
lines = input.readlines()

monkeys = []

for i in range(0, len(lines), 7):
    monkey = {}
    monkey['num'] = int(lines[i].split()[1].split(':')[0])
    monkey['items'] = deque()
    items = lines[i+1].split(': ')[1].split(', ')
    for item in items:
        monkey['items'].append(int(item))
    monkey['operation'] = lines[i+2].split(' = ')[1].strip()
    monkey['test'] = int(lines[i+3].split()[3])
    monkey['if_true'] = int(lines[i+4].split()[5])
    monkey['if_false'] = int(lines[i+5].split()[5])
    print(monkey)
    monkeys.append(monkey)

lcm = math.lcm(5, 2, 13, 7, 19, 11, 3, 17)
inspections = [0 for i in range(0, len(monkeys))]

for round in range(0,10000):
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            old = monkey['items'].popleft()
            inspections[monkey['num']] += 1
            new = eval(monkey['operation'])
            # new = new // 3
            new = new % lcm # Found a new way of managing my worry
            if new % monkey['test'] == 0:
                monkeys[monkey['if_true']]['items'].append(new)
            else:
                monkeys[monkey['if_false']]['items'].append(new)

inspections.sort()
sum = inspections[len(inspections) - 1] * inspections[len(inspections) - 2]
print(sum)
