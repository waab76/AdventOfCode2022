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
    # print('Sensor at [{},{}], beacon at [{},{}]\n  Range is {}'.format(sensor['x'],sensor['y'],beacon_x,beacon_y,sensor['range']))
    sensors.append(sensor)
