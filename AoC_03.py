def get_priority(char):
    priority = ord(char)
    if priority >= 97: # 'a' is 97 but we want 1
        return (priority - 96)
    else: # 'A' is 65 but we want 26
        return (priority - 38)

input = open('input_03', 'r')
lines = input.readlines()

priority_sum = 0
for line in lines:
    for item in line[:len(line)//2]:
        if item in line[len(line)//2:]:
            priority_sum += get_priority(item)
            break
print(priority_sum)

badge_sum = 0
for i in range(0, len(lines), 3):
    for item in lines[i]:
        if item in lines[i+1]:
            if item in lines[i+2]:
                badge_sum += get_priority(item)
                break
print(badge_sum)
