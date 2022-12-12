input = open('input_04', 'r')
lines = input.readlines()

full_overlaps = 0
all_overlaps = 0

for line in lines:
    ranges = line.strip().split(',')
    first = set(range(int(ranges[0].split('-')[0]), int(ranges[0].split('-')[1])+1))
    second = set(range(int(ranges[1].split('-')[0]), int(ranges[1].split('-')[1])+1))
    if len(first.intersection(second)) in [len(first), len(second)]:
        full_overlaps += 1

    if len(first.intersection(second)) > 0:
        all_overlaps += 1

print('Full: {}'.format(full_overlaps))
print('All: {}'.format(all_overlaps))
