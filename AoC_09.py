input = open('input_09','r')
lines = input.readlines()

knot_count = 10

knots = [[0,0] for i in range(0,knot_count)]

visited = set()

for line in lines:
    direction = line.split()[0]
    steps = int(line.split()[1])

    # print('Head moving {} steps {}'.format(steps, direction))
    for i in range(0,steps):
        if direction == 'U':
            knots[0][1] += 1
        elif direction == 'D':
            knots[0][1] -= 1
        elif direction == 'R':
            knots[0][0] += 1
        elif direction == 'L':
            knots[0][0] -= 1
        else:
            print('Fucked up on direction')

        for i in range(1, knot_count):
            if knots[i-1][0] == knots[i][0]:
                if knots[i-1][1] == knots[i][1] + 2:
                    knots[i][1] += 1
                elif knots[i-1][1] == knots[i][1] - 2:
                    knots[i][1] -= 1
                elif abs(knots[i-1][0] - knots[i][0]) <= 1 and abs(knots[i-1][1] - knots[i][1]) <= 1:
                    continue
                    # print('Touching')
                else:
                    print('Fucked up on same X')
            elif knots[i-1][1] == knots[i][1]:
                if knots[i-1][0] == knots[i][0] + 2:
                    knots[i][0] += 1
                if knots[i-1][0] == knots[i][0] - 2:
                    knots[i][0] -= 1
                elif abs(knots[i-1][0] - knots[i][0]) <= 1 and abs(knots[i-1][1] - knots[i][1]) <= 1:
                    continue
                    # print('Touching')
                else:
                    print('Fucked up on same Y')
            elif (knots[i-1][0] == knots[i][0] + 1 and knots[i-1][1] == knots[i][1] + 2) \
            or (knots[i-1][0] == knots[i][0] + 2 and knots[i-1][1] == knots[i][1] + 1) \
            or (knots[i-1][0] == knots[i][0] + 2 and knots[i-1][1] == knots[i][1] + 2):
                knots[i][0] += 1
                knots[i][1] += 1
            elif (knots[i-1][0] == knots[i][0] - 1 and knots[i-1][1] == knots[i][1] + 2) \
            or (knots[i-1][0] == knots[i][0] - 2 and knots[i-1][1] == knots[i][1] + 1) \
            or (knots[i-1][0] == knots[i][0] - 2 and knots[i-1][1] == knots[i][1] + 2):
                knots[i][0] -= 1
                knots[i][1] += 1
            elif (knots[i-1][0] == knots[i][0] + 1 and knots[i-1][1] == knots[i][1] - 2) \
            or (knots[i-1][0] == knots[i][0] + 2 and knots[i-1][1] == knots[i][1] - 1) \
            or (knots[i-1][0] == knots[i][0] + 2 and knots[i-1][1] == knots[i][1] - 2):
                knots[i][0] += 1
                knots[i][1] -= 1
            elif (knots[i-1][0] == knots[i][0] - 1 and knots[i-1][1] == knots[i][1] - 2) \
            or (knots[i-1][0] == knots[i][0] - 2 and knots[i-1][1] == knots[i][1] - 1) \
            or (knots[i-1][0] == knots[i][0] - 2 and knots[i-1][1] == knots[i][1] - 2):
                knots[i][0] -= 1
                knots[i][1] -= 1
            elif abs(knots[i-1][0] - knots[i][0]) <= 1 and abs(knots[i-1][1] - knots[i][1]) <= 1:
                continue
                # print('Touching')
            else:
                print('Fucked up on diagonal. Knot {} [{},{}] Knot {} [{},{}]'.format(i - 1, knots[i-1][0], knots[i-1][1], i, knots[i][0], knots[i][1]))

        # print('Tail at [{},{}]'.format(knots[len(knots) - 1][0],knots[len(knots) - 1][1]))
        visited.add('[{},{}]'.format(knots[knot_count - 1][0], knots[knot_count - 1][1]))

# print(visited)
print(len(visited))
