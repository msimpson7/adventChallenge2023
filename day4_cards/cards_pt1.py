
input_file = 'puzzle_input.txt'

try:
    with open(input_file, 'r') as my_file:
        file_info = my_file.readlines()
except FileNotFoundError as e:
    print(f'Could not find file -- {e}')

summation = 0

# Input the card's winning numbers, then the playing number
# Evaluate how many numbers are shared
# Point value is 2**(n-1), where n is the number of matches

for line in file_info:
    lottery_info = line.split(':')[1]
    lottery1 = lottery_info.split('|')
    winning = [int(i) for i in lottery1[0].split() if i.isdigit()]
    test_nums = [int(i) for i in lottery1[1].split() if i.isdigit()]
    winning_set = set(winning) & set(test_nums)
    # print(f'{winning}\n{test_nums}')
    # print(f'{winning_set} -- {len(winning_set)} -- {2**(len(winning_set)-1)}\n')

    if len(winning_set) > 0:
        summation += 2**(len(winning_set)-1)

print(f'The summation of the winning cards is {summation}')

