import re

pattern = re.compile('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

input = open('input_15','r')
lines = input.readlines()

sensors = []
for line in lines:
    sensor = {}
    match = pattern.match(line)
    sensor['x'] = int(match.group(1))
    sensor['y'] = int(match.group(2))
    beacon_x = int(match.group(3))
    beacon_y = int(match.group(4))
    sensor['range'] = abs(sensor['x'] - beacon_x) + abs(sensor['y'] - beacon_y)
    sensors.append(sensor)

target_row = 2000000
covered = set()
for sensor in sensors:
    y_diff = abs(sensor['y'] - target_row)
    if y_diff <= sensor['range']:
        cover_left = sensor['x'] - (sensor['range'] - y_diff)
        cover_right = sensor['x'] + (sensor['range'] - y_diff)
        for i in range(cover_left, cover_right + 1):
            covered.add(i)
print(len(covered))

for y in range(0,4000001):
    x = 0
    coverage = []
    for sensor in sensors:
        y_diff = abs(sensor['y'] - y)
        if y_diff <= sensor['range']:
            cover_left = sensor['x'] - (sensor['range'] - y_diff)
            cover_right = sensor['x'] + (sensor['range'] - y_diff)
            coverage.append((cover_left,cover_right))
    coverage.sort()
    while x < 4000001:
        for range in coverage:
            if x >= range[0] and x <= range[1]:
                x = range[1] + 1
            elif x < range[0]:
                print(4000000 * x + y)
                quit()
