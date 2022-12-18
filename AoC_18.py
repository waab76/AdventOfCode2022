from collections import deque

input = open('input_18','r')
lines = input.readlines()

max_x = -1
max_y = -1
max_z = -1

magma = 'X'
open = ' '
steam = '~'

for line in lines:
    line.strip()
    coords = line.split(',')
    if int(coords[0]) > max_x:
        max_x = int(coords[0])
    if int(coords[1]) > max_y:
        max_y = int(coords[1])
    if int(coords[2]) > max_z:
        max_z = int(coords[2])
max_x += 5
max_y += 5
max_z += 5

lava = [[[open for i in range(0,max_z + 1)] for i in range(0,max_y + 1)] for i in range(0,max_x + 1)]
surface_area = 0

for line in lines:
    coords = line.split(',')
    x = int(coords[0]) + 1
    y = int(coords[1]) + 1
    z = int(coords[2]) + 1
    surface_area += 6
    lava[x][y][z] = magma
    if lava[x][y][z + 1] == magma:
        surface_area -= 2
    if lava[x][y][z - 1] == magma:
        surface_area -= 2
    if lava[x][y + 1][z] == magma:
        surface_area -= 2
    if lava[x][y - 1][z] == magma:
        surface_area -= 2
    if lava[x + 1][y][z] == magma:
        surface_area -= 2
    if lava[x - 1][y][z] == magma:
        surface_area -= 2
print(surface_area)

to_steam = deque([(0,0,0)])
while len(to_steam) > 0:
    # print('{} cells left to steam'.format(len(to_steam)))
    cell = to_steam.popleft()
    x = cell[0]
    y = cell[1]
    z = cell[2]
    # print('Checking ({},{},{})'.format(x,y,z))
    if lava[x][y][z] == magma or lava[x][y][z] == steam:
        continue
    lava[x][y][z] = steam
    if x > 0:
        to_steam.append((x - 1, y, z))
    if x < max_x - 1:
        to_steam.append((x + 1, y, z))
    if y > 0:
        to_steam.append((x, y - 1, z))
    if y < max_y - 1:
        to_steam.append((x, y + 1, z))
    if z > 0:
        to_steam.append((x, y, z - 1))
    if z < max_z - 1:
        to_steam.append((x, y, z + 1))

# for x in range(0, max_x):
#     print('{} - {} - {} - {} - {} - {} - {} - {}'.format(x,x,x,x,x,x,x,x))
#     for y in range(0, max_y):
#         print(' '.join(lava[x][y]))

sa2 = 0
for line in lines:
    coords = line.split(',')
    x = int(coords[0]) + 1
    y = int(coords[1]) + 1
    z = int(coords[2]) + 1
    if lava[x][y][z + 1] == steam:
        sa2 += 1
    if lava[x][y][z - 1] == steam:
        sa2 += 1
    if lava[x][y + 1][z] == steam:
        sa2 += 1
    if lava[x][y - 1][z] == steam:
        sa2 += 1
    if lava[x + 1][y][z] == steam:
        sa2 += 1
    if lava[x - 1][y][z] == steam:
        sa2 += 1
print(sa2)
