input = open('input_10', 'r')
lines = input.readlines()

x = 1
cycle = 1
sum = 0

display = [['.' for i in range(0,40)] for j in range(0,6)]

for line in display:
    print(''.join(line))

for line in lines:
    if 'noop' in line:
        # print('Noop - cycle {} x is {}'.format(cycle, x))
        if cycle in [20, 60, 100, 140, 180, 220]:
            sum += cycle * x
            # print('Cycle {} x sum {}'.format(cycle, sum))
        if (cycle - 1) % 40 in [x - 1, x, x + 1]:
            display[(cycle - 1) // 40][(cycle - 1) % 40] = '#'
        cycle += 1
    elif 'addx' in line:
        add_amt = int(line.strip().split()[1])
        # print('Addx {} - cycle {} x is {}'.format(add_amt, cycle, x))
        if cycle in [20, 60, 100, 140, 180, 220]:
            sum += cycle * x
            # print('Cycle {} x sum {}'.format(cycle, sum))
        if (cycle - 1) % 40 in [x - 1, x, x + 1]:
            display[(cycle - 1) // 40][(cycle - 1) % 40] = '#'
        cycle += 1
        # print('Addx {} - cycle {} x is {}'.format(add_amt, cycle, x))
        if cycle in [20, 60, 100, 140, 180, 220]:
            sum += cycle * x
            # print('Cycle {} x sum {}'.format(cycle, sum))
        if (cycle - 1) % 40 in [x - 1, x, x + 1]:
            display[(cycle - 1) // 40][(cycle - 1) % 40] = '#'
        cycle += 1
        x += add_amt

print(sum)
for line in display:
    print(''.join(line))
