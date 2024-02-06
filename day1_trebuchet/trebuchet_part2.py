import re

input_file = 'test.txt'


def change_to_num(num_char):
    if len(num_char) == 1:
        return num_char
    elif num_char == "one":
        return "1"
    elif num_char == "two":
        return "2"
    elif num_char == "three":
        return "3"
    elif num_char == "four":
        return "4"
    elif num_char == "five":
        return "5"
    elif num_char == "six":
        return "6"
    elif num_char == "seven":
        return "7"
    elif num_char == "eight":
        return "8"
    elif num_char == "nine":
        return "9"
    else:
        return "Not a number"


def get_numbers(line):
    pattern = "(\\d)?(one)?(two)?(three)?(four)?(five)?(six)?(seven)?(eight)?(nine)?"
    pattern_reverse = "(\\d)?(eno)?(owt)?(eerht)?(ruof)?(evif)?(xis)?(neves)?(thgie)?(enin)?"
    first_num = re.search(pattern, line)[0]
    last_num = re.search(pattern_reverse, line[::-1].replace("\n", ""))[0]
    print(f"first_num is '{first_num}', last_num is '{last_num}'")
    return int(change_to_num(first_num) + change_to_num(last_num[::-1]))


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
