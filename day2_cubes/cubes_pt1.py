import re

input_file = 'puzzle_input.txt'


def get_game_id(line):
    return int(re.search("Game (\\d+):", line)[1])


def valid_game(line):
    max_red = 12
    max_green = 13
    max_blue = 14
    valid = True
    no_id = line.split(':')[1]
    pulls = no_id.split(';')
    for pull in pulls:
        cubes = pull.split(',')
        for cube in cubes:
            cube = cube.strip()
            num_color = cube.partition(' ')
            num = int(num_color[0])
            color = num_color[2]
            if color == 'red' and num > max_red:
                valid = False
            elif color == 'green' and num > max_green:
                valid = False
            elif color == 'blue' and num > max_blue:
                valid = False

    return valid


try:
    with open(input_file, 'r') as my_file:
        file_info = my_file.readlines()
except FileNotFoundError as e:
    print(f'Could not find file -- {e}')

summation = 0

for line in file_info:
    game_id = get_game_id(line)
    if valid_game(line):
        print(f'Game {game_id} is valid')
        summation += game_id
    else:
        print(f'Game {game_id} is NOT valid')

print(f"The sum of the game ids is {summation}")
