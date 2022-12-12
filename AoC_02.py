# A = Rock, B = Paper, C = Scissors
# X = Rock 1, Y = Paper 2, Z = Scissors 3
# round_score = {'A': {'X': 4, 'Y': 8, 'Z': 3}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 7, 'Y': 2, 'Z': 6}}

# Revised X = Lose, Y = Draw, Z = Win
round_score = {'A': {'X': 3, 'Y': 4, 'Z': 8}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 2, 'Y': 6, 'Z': 7}}

input = open('input_02', 'r')
lines = input.readlines()

score = 0

for line in lines:
    round = line.strip().split()
    score += round_score[round[0]][round[1]]

print(score)
