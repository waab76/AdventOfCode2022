from collections import deque

input = open('input_12', 'r')
lines = input.readlines()

for line in lines:
    line.strip()

start = {}
end = {}

elev = [[0 for i in range(0, len(lines[0]))] for j in range(0,len(lines))]
path = [[10000 for i in range(0,len(lines[0]))] for j in range(0,len(lines))]

for y in range(0,len(lines)):
    for x in range(0,len(lines[y])):
        if lines[y][x] == 'S':
            start['x'] = x
            start['y'] = y
            elev[y][x] = 0
        elif lines[y][x] == 'E':
            end['x'] = x
            end['y'] = y
            elev[y][x] = 25
        else:
            elev[y][x] = ord(lines[y][x]) - ord('a')

path[end['y']][end['x']] = 0
to_check = deque()
to_check.append(end)

while len(to_check) > 0:
    checking = to_check.popleft()
    # Check up
    if checking['y'] - 1 >= 0 \
    and elev[checking['y'] - 1][checking['x']] >= elev[checking['y']][checking['x']] - 1 \
    and path[checking['y'] - 1][checking['x']] > path[checking['y']][checking['x']] + 1:
        path[checking['y'] - 1][checking['x']] = path[checking['y']][checking['x']] + 1
        to_check.append({'x': checking['x'], 'y': checking['y'] - 1})
    # Check down
    if checking['y'] + 1 < len(elev) \
    and elev[checking['y'] + 1][checking['x']] >= elev[checking['y']][checking['x']] - 1 \
    and path[checking['y'] + 1][checking['x']] > path[checking['y']][checking['x']] + 1:
        path[checking['y'] + 1][checking['x']] = path[checking['y']][checking['x']] + 1
        to_check.append({'x': checking['x'], 'y': checking['y'] + 1})
    # Check left
    if checking['x'] - 1 >= 0 \
    and elev[checking['y']][checking['x'] - 1] >= elev[checking['y']][checking['x']] - 1 \
    and path[checking['y']][checking['x'] - 1] > path[checking['y']][checking['x']] + 1:
        path[checking['y']][checking['x'] - 1] = path[checking['y']][checking['x']] + 1
        to_check.append({'x': checking['x'] - 1, 'y': checking['y']})
    # Check right
    if checking['x'] + 1 < len(elev[0]) \
    and elev[checking['y']][checking['x'] + 1] >= elev[checking['y']][checking['x']] - 1 \
    and path[checking['y']][checking['x'] + 1] > path[checking['y']][checking['x']] + 1:
        path[checking['y']][checking['x'] + 1] = path[checking['y']][checking['x']] + 1
        to_check.append({'x': checking['x'] + 1, 'y': checking['y']})

print(path[start['y']][start['x']])

min_path = path[start['y']][start['x']]
for i in range(0, len(elev)):
    for j in range(0, len(elev[i])):
        if elev[i][j] == 0 and path[i][j] < min_path:
            min_path = path[i][j]
print(min_path)
