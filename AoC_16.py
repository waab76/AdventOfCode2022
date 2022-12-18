import re

input = open('input_16','r')
lines = input.readlines()

pattern = re.compile('Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)')

valves = {}
curr_valve = 'AA'
visited = set([curr_valve])

for line in lines:
    match = pattern.match(line)
    # print(match.group(0))
    valve = {}
    valve['label'] = match.group(1)
    valve['flow'] = int(match.group(2))
    valve['neighbors'] = match.group(3).split(', ')
    valves[valve['label']] = valve
