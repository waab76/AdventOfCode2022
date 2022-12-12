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

print('Start at [{}] - End at [{}]'.format(start, end))

path[end['y']][end['x']] = 0
