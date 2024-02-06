
input_file = 'puzzle_input.txt'


def get_least_product(line):
    min_red = min_green = min_blue = 1
    no_id = line.split(':')[1]
    pulls = no_id.split(';')
    for pull in pulls:
        cubes = pull.split(',')
        for cube in cubes:
            cube = cube.strip()
            num_color = cube.partition(' ')
            num = int(num_color[0])
            color = num_color[2]
            if color == 'red' and num > min_red:
                min_red = num
            elif color == 'green' and num > min_green:
                min_green = num
            elif color == 'blue' and num > min_blue:
                min_blue = num

    return min_red * min_green * min_blue

try:
    with open(input_file, 'r') as my_file:
        file_info = my_file.readlines()
except FileNotFoundError as e:
    print(f'Could not find file -- {e}')

summation = 0

for line in file_info:
    num = get_least_product(line)
    summation += num

print(f'The sum of the products is {summation}')
