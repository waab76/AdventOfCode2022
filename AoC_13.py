import functools
def compare(left, right):
    # print('Comparing:\n  {}\n  {}'.format(left, right))
    if isinstance(left, list) and isinstance(right, list):
        # print('Both lists, doing length check')
        if len(left) == 0 and len(right) == 0:
            # print('Both empty, equal')
            return 0
        elif len(left) == 0:
            # print('Left empty, in order')
            return -1
        elif len(right) == 0:
            # print('Right empty, out of order')
            return 1
        else:
            # print('Neither empty, comparing first elements')
            left_item = left[0]
            left = left[1:]
            right_item = right[0]
            right = right[1:]
            result = compare(left_item, right_item)
            if result == 0:
                # print('Elements were equal, continuing with remainder')
                return compare(left, right)
            else:
                return result
    elif isinstance(left, list):
        # print('Left is a list, recursing')
        return compare(left, [right])
    elif isinstance(right, list):
        # print('Right is a list, recursing')
        return compare([left], right)
    else:
        if left < right:
            # print('Left item is lower, in order')
            return -1
        elif left > right:
            # print('Right item is lower, out of order')
            return 1
        else:
            # print('Left and Right are equal')
            return 0

input = open('input_13','r')
lines = input.readlines()

for line in lines:
    line.strip()

index = 0
sum = 0

for i in range(0, len(lines), 3):
    index += 1
    left = eval(lines[i])
    right = eval(lines[i+1])
    if compare(left, right) == -1:
        # print('Packet set {} is in order'.format(index))
        sum += index
print('Part 1: {}'.format(sum))

to_sort = []
to_sort.append([[2]])
to_sort.append([[6]])
for i in range(0, len(lines), 3):
        to_sort.append(eval(lines[i]))
        to_sort.append(eval(lines[i+1]))
sorted = sorted(to_sort, key=functools.cmp_to_key(compare))
first = 0
second = 0
for i in range(0,len(sorted)):
    if sorted[i] == [[2]]:
        first = i+1
    elif sorted[i] == [[6]]:
        second = i+1
        break
print('Part 2: {}'.format(first * second))
