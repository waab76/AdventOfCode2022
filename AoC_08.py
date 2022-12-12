input = open('input_08', 'r')
lines = input.readlines()

for row in range(0, len(lines)):
    lines[row] = lines[row].strip()

rows = len(lines)
cols = len(lines[0])
visible = [[0 for x in range(0, cols)] for y in range(0,rows)]
trees = [[0 for x in range(0, cols)] for y in range(0,rows)]
for row in range(0,rows):
    for col in range(0,cols):
        trees[row][col] = int(lines[row][col])

for row in range(0,rows):
    max = -1
    for col in range(0,cols):
        if trees[row][col] > max:
            max = trees[row][col]
            visible[row][col] = 1
    max = -1
    for col in reversed(range(0,cols)):
        if trees[row][col] > max:
            max = trees[row][col]
            visible[row][col] = 1

for col in range(0,cols):
    max = -1
    for row in range(0,rows):
        if trees[row][col] > max:
            max = trees[row][col]
            visible[row][col] = 1
    max = -1
    for row in reversed(range(0,rows)):
        if trees[row][col] > max:
            max = trees[row][col]
            visible[row][col] = 1

sum = 0
for row in range(0,rows):
    for col in range(0,cols):
        sum += visible[row][col]

print(sum)

def scenic_score(my_row,my_col):
    right = 0
    for col in range(my_col + 1, cols):
        if trees[my_row][col] < trees[my_row][my_col]:
            right += 1
        elif trees[my_row][col] == trees[my_row][my_col]:
            right += 1
            break
    left = 0
    for col in reversed(range(0, my_col)):
        if trees[my_row][col] < trees[my_row][my_col]:
            left += 1
        elif trees[my_row][col] == trees[my_row][my_col]:
            left += 1
            break
    down = 0
    for row in range(my_row + 1, rows):
        if trees[row][my_col] < trees[my_row][my_col]:
            down += 1
        elif trees[row][my_col] == trees[my_row][my_col]:
            down += 1
            break
    up = 0
    for row in reversed(range(0, my_row)):
        if trees[row][my_col] < trees[my_row][my_col]:
            up += 1
        elif trees[row][my_col] == trees[my_row][my_col]:
            up += 1
            break
    return right * left * down * up

max_scenic = -1
for row in range(0,rows):
    for col in range(0,cols):
        scenic = scenic_score(row,col)
        if scenic > max_scenic:
            max_scenic = scenic
print(max_scenic)
