import re

input_file = 'puzzle_input.txt'


def get_numbers(line):
    first_num = re.search("\\d", line)[0]
    last_num = re.search('\\d', line[::-1])[0]
    return int(first_num + last_num)


def clean_line(line):
    updated_line = (line.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e')
                    .replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x')
                    .replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e'))

    return updated_line


try:
    with open(input_file, 'r') as my_file:
        file_info = my_file.readlines()
except FileNotFoundError as e:
    print(f'Could not find file -- {e}')

summation = 0
for line in file_info:
    new_line = clean_line(line)
    number = get_numbers(new_line)
    summation += number
print(f'The sum of the numbers is: {summation}')
