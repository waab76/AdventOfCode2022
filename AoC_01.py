input = open('input_01', 'r')
lines = input.readlines()

currElf = 0
maxElf = 0
elves = []

for line in lines:
    try:
        currSnack = int(line.strip())
        currElf += currSnack
    except:
        elves.append(currElf)
        if currElf > maxElf:
            print(currElf, 'is more than', maxElf, ' - We have a new leader')
            maxElf = currElf
        currElf = 0

print(maxElf)

elves.sort(reverse=True)
top_three = elves[0] + elves[1] + elves[2]

print(top_three)
