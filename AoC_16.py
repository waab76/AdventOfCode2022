import re

input = open('input_16','r')
lines = input.readlines()

pattern = re.compile('Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)')
valves = {}

for line in lines:
    match = pattern.match(line)
    valve = {}
    valve['label'] = match.group(1)
    valve['flow'] = int(match.group(2))
    valve['neighbors'] = match.group(3).split(', ')
    valves[valve['label']] = valve

def eval(valve, minute, valves_on, prev):
    if minute > 30:
        return 0
    options = []
    if valve['label'] not in valves_on and valve['flow'] > 0:
        for neighbor in valve['neighbors']:
            if len(valves[neighbor]['neighbors']) > 1 or (valves[neighbor]['flow'] > 0 and neighbor not in valves_on):
                options.append(valve['flow'] * (30 - minute) + eval(valves[neighbor], minute + 2, valves_on + [valve['label']], valve['label']))
    for neighbor in valve['neighbors']:
        if prev != neighbor and (len(valves[neighbor]['neighbors']) > 1 or (valves[neighbor]['flow'] > 0 and neighbor not in valves_on)):
            options.append(eval(valves[neighbor], minute + 1, valves_on, valve['label']))
    if len(options) == 0:
        return 0
    return max(options)
# print(eval(valves['AA'], 1, [], ''))

def distance(start, end):
    reachable = set(valves[start]['neighbors'])
    steps = 1
    while end not in reachable:
        steps += 1
        more_valves = []
        for valve in reachable:
            more_valves += valves[valve]['neighbors']
        reachable.update(more_valves)
    return steps

sorted_valves = list(reversed(sorted(valves.values(), key=lambda d: d['flow'])))
edge_weights = {}

for start in sorted_valves:
    edge_weights[start['label']] = {}
    for end in sorted_valves:
        if start['label'] == end['label']:
            edge_weights[start['label']][end['label']] = 0
        else:
            edge_weights[start['label']][end['label']] = distance(start['label'],end['label'])

flow_valves = {}
for valve in valves.values():
    if valve['flow'] > 0 or valve['label'] in ['AA']:
        flow_valves[valve['label']] = valve

def eval2(valve, minute, valves_on):
    if minute > 30:
        return 0
    options = []
    for available in flow_valves.values():
        if available['flow'] > 0 and available['label'] not in valves_on:
            my_flow = valves[valve]['flow'] * (30 - minute - 1)
            time_to_next = edge_weights[valves[valve]['label']][available['label']]
            options.append(my_flow + eval2(available['label'], minute + 1 + time_to_next, valves_on + [valve]))
    if len(options) == 0:
        return 0
    return max(options)

print(eval2('AA', 0, []))
