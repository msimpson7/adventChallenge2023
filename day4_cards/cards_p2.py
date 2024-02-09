import math

input_file = 'puzzle_input.txt'

try:
    with open(input_file, 'r') as my_file:
        file_info = my_file.readlines()
except FileNotFoundError as e:
    print(f'Could not find file -- {e}')

scorecards = []
for i in range(len(file_info)):
    scorecards.append(1)

i = 0
for line in file_info:
    lottery_info = line.split(':')[1]
    lottery1 = lottery_info.split('|')
    winning = [int(i) for i in lottery1[0].split() if i.isdigit()]
    test_nums = [int(i) for i in lottery1[1].split() if i.isdigit()]
    winning_set = set(winning) & set(test_nums)

    if len(winning_set) > 0:
        for j in range(len(winning_set)):
            scorecards[i+j+1] += scorecards[i]
    i += 1

summation = int(math.fsum(scorecards))
print(f'The summation of number of scorecards is {summation}')
