input = open('input_20','r')
lines = input.readlines()

def print_list(head_ptr):
    print_me = head_ptr
    print_list = []
    for i in range(0, len(lines)):
        print_list.append(str(print_me['val']))
        print_me = print_me['mixed_next']
    print(', '.join(print_list))

def find_zero(head_ptr):
    to_list = head_ptr
    zero_pos = -1
    for i in range(0, len(lines)):
        if to_list['val'] == 0:
            return i
        to_list = to_list['mixed_next']
    raise Exception('Could not find the 0')

head = None
curr = None

decryption_key = 1 # 811589153

for line in lines:
    line.strip()
    num = int(line)
    new = {}
    new['val'] = num * decryption_key
    new['orig_next'] = None
    new['mixed_next'] = None
    new['orig_prev'] = None
    new['mixed_prev'] = None
    new['mixed'] = False
    if head == None:
        head = new
    if curr == None:
        curr = head
    else:
        new['orig_prev'] = curr
        new['mixed_prev'] = curr
        curr['orig_next'] = new
        curr['mixed_next'] = new
        curr = new
curr['orig_next'] = head
curr['mixed_next'] = head
head['orig_prev'] = curr
head['mixed_prev'] = curr

mix_count = 1

# print_list(head)

for mix in range(0,mix_count):
    print('Doing mix {}'.format(mix + 1))
    mix_next = head
    num_mixed = 0
    while num_mixed < len(lines):
        mix_ptr = mix_next
        mix_next = mix_next['orig_next']
        if mix_ptr['mixed']:
            continue
        elif mix_ptr['val'] == 0:
            # print('0 at position {} between {} (next {}) and {} (prev {}) mid-mix'.format(find_zero(head), mix_next['mixed_prev']['val'], mix_next['mixed_prev']['mixed_next']['val'], mix_next['mixed_next']['val'], mix_next['mixed_next']['mixed_prev']['val']))
            mix_ptr['mixed'] = True
            num_mixed += 1
            continue
        mix_me = mix_ptr.copy()
        mix_ptr['mixed_prev']['mixed_next'] = mix_ptr['mixed_next']
        mix_ptr['mixed_next']['mixed_prev'] = mix_ptr['mixed_prev']

        if mix_me['val'] > 0:
            for i in range(0, abs(mix_me['val']) % (len(lines) - 1)):
                mix_ptr = mix_ptr['mixed_next']
            mix_me['mixed_next'] = mix_ptr['mixed_next']
            mix_me['mixed_prev'] = mix_ptr
            mix_ptr['mixed_next']['mixed_prev'] = mix_me
            mix_ptr['mixed_next'] = mix_me
            mix_me['mixed'] = True
            num_mixed += 1
        else:
            for i in range(0, abs(mix_me['val']) % (len(lines) - 1)):
                mix_ptr = mix_ptr['mixed_prev']
            mix_me['mixed_next'] = mix_ptr
            mix_me['mixed_prev'] = mix_ptr['mixed_prev']
            mix_ptr['mixed_prev']['mixed_next'] = mix_me
            mix_ptr['mixed_prev'] = mix_me
            mix_me['mixed'] = True
            num_mixed += 1

    # print_list(head)

    reset = head
    for i in range(0,len(lines)):
        reset['mixed'] = False
        reset = reset['orig_next']

mixed_nums = []
to_list = head
zero_pos = find_zero(head)
for i in range(0, len(lines)):
    mixed_nums.append(to_list['val'])
    to_list = to_list['mixed_next']

print('0 in position {}'.format(zero_pos))
print('1000th past 0 is {}'.format(mixed_nums[(zero_pos + 1000) % len(lines)]))
print('2000th past 0 is {}'.format(mixed_nums[(zero_pos + 2000) % len(lines)]))
print('3000th past 0 is {}'.format(mixed_nums[(zero_pos + 3000) % len(lines)]))

sum = mixed_nums[(zero_pos + 1000) % len(lines)] + mixed_nums[(zero_pos + 2000) % len(lines)] + mixed_nums[(zero_pos + 3000) % len(lines)]
print(sum)
