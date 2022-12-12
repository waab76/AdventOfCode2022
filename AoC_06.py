from collections import deque

input = open('input_06', 'r')
lines = input.readlines()

marker_size = 14

for line in lines:
    q = deque([], maxlen=marker_size - 1)

    for i in range(0,len(line)):
        # print('Sliding window is {} next is {}'.format(q, line[i]))
        if len(q) == marker_size - 1 and len(set(q)) == len(q) and line[i] not in q:
            print(i + 1)
            break
        else:
            q.append(line[i])
