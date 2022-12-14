def print_grid(grid):
    for line in grid:
        print(''.join(line))

input = open('input_14','r')
lines = input.readlines()

min_x = 500
max_x = 500
max_y = 0

for line in lines:
    line.strip()
    points = line.split(' -> ')
    for point in points:
        x = int(point.split(',')[0])
        y = int(point.split(',')[1])
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

min_x -= 250
max_x += 250
max_y += 2

# print('X range {} to {}\nY range 0 to {}'.format(min_x, max_x, max_y))

cave = [['.' for x in range(0, max_x - min_x + 1)] for y in range(0, max_y + 1)]

for x in range(0, max_x - min_x + 1):
    cave[max_y][x] = '#'

for line in lines:
    points = line.split(' -> ')
    start_x = int(points[0].split(',')[0]) - min_x
    start_y = int(points[0].split(',')[1])
    for rock_line in range(1, len(points)):
        next_x = int(points[rock_line].split(',')[0]) - min_x
        next_y = int(points[rock_line].split(',')[1])
        # print('Rock from [{},{}] to [{},{}]'.format(start_x, start_y, next_x, next_y))
        for x in range(min(start_x, next_x), max(start_x, next_x) + 1):
            for y in range(min(start_y, next_y), max(start_y, next_y) + 1):
                cave[y][x] = '#'
        start_x = next_x
        start_y = next_y
cave[0][500 - min_x] = '+'

# print_grid(cave)

units_dropped = 0
units_voided = 0
can_drop = True

# while units_voided == 0:
while can_drop:
    units_dropped += 1
    sand_x = 500 - min_x
    sand_y = 0
    sand_falling = True

    while sand_falling:
        try:
            if cave[sand_y + 1][sand_x] not in ['o','#']:
                sand_y += 1
            elif cave[sand_y + 1][sand_x - 1] not in ['o','#']:
                sand_y += 1
                sand_x -= 1
            elif cave[sand_y + 1][sand_x + 1] not in ['o','#']:
                sand_y += 1
                sand_x += 1
            else:
                cave[sand_y][sand_x] = 'o'
                sand_falling = False
                if sand_x == 500 - min_x and sand_y == 0:
                    can_drop = False

        except IndexError:
            # units_voided += 1
            # break
            print('Ran out of room')
            quit()
    # print_grid(cave)
print(units_dropped - units_voided)
