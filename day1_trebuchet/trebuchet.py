import re

input_file = 'puzzle_input.txt'


def get_numbers(line):
    first_num = re.search("\\d", line)[0]
    last_num = re.search('\\d', line[::-1])[0]
    return int(first_num + last_num)


try:
    with open(input_file, 'r') as my_file:
        file_info = my_file.readlines()
except FileNotFoundError as e:
    print(f'Could not find file -- {e}')

summation = 0
for line in file_info:
    number = get_numbers(line)
    summation += number
print(f'The sum of the numbers is: {summation}')
