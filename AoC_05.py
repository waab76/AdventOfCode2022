import re

input = open('input_05', 'r')
lines = input.readlines()

move = re.compile('move (\d*) from (\d*) to (\d*)')
state = 0
stacks = [[], [], [], [], [], [], [], [], []]

for line in lines:
    if state == 0:
        print('Processing line {}'.format(line.strip()))
        if '1   2   3   4   5   6   7   8   9' in line:
            state += 1
            continue
        for i in range(1, 34, 4):
            try:
                if ' ' != line[i]:
                    stacks[(i-1)//4].append(line[i])
            except:
                break
    elif state == 1:
        print('Cleanup time!')
        for i in range(0,9):
            stacks[i].reverse()
        print('Stacks are {}'.format(stacks))
        state += 1
    elif state == 2:
        # print('Processing line {}'.format(line.strip()))
        match = move.match(line.strip())
        if match:
            count = int(match.group(1))
            move_from = int(match.group(2)) - 1
            move_to = int(match.group(3)) - 1

            temp_stack = []
            for i in range(0,count):
                item = stacks[move_from].pop()
                temp_stack.append(item)
            for i in range(0, len(temp_stack)):
                item = temp_stack.pop()
                stacks[move_to].append(item)

out = ''
for i in range(0,9):
    out += stacks[i].pop()

print(out)
