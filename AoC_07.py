input = open('input_07', 'r')
lines = input.readlines()

directories = {}
curr_path = []

for line in lines:
    curr_full_path = '/{}'.format('/'.join(curr_path))
    if curr_full_path not in directories:
        directories[curr_full_path] = 0
    if line.startswith('$ cd'):
        target_dir = line.split()[2]
        if target_dir == '..':
            curr_path.pop()
        elif target_dir == '/':
            curr_path = []
        else:
            curr_path.append(target_dir)
    elif line.startswith('$ ls'):
        continue
    elif line.startswith('dir'):
        found_dir = line.split()[1]
    else:
        file_name = line.split()[1]
        file_size = int(line.split()[0])
        for i in range(0, len(curr_path)+1):
            dir = '/{}'.format('/'.join(curr_path[:i]))
            directories[dir] += file_size

total_bytes = 0
for directory in directories:
    if directories[directory] < 100000:
        total_bytes += directories[directory]

print(total_bytes)

free_space = 70000000 - directories['/']
min_delete = 30000000 - free_space

smallest_dir = '/'
smallest_dir_size = directories[smallest_dir]
for dir in directories:
    if directories[dir] >= min_delete and directories[dir] < smallest_dir_size:
        smallest_dir = dir
        smallest_dir_size = directories[smallest_dir]
        
print(smallest_dir_size)
