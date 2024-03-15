import os, shelve
input_file = 'puzzle_input.txt'
output_dir = 'seeds'


def build_list(shelf, units):
    for i in range(units[2]):
        shelf[str(units[1])] = units[0]
        # list_builder.write(f'({units[1]}, {units[0]}), ')
        units[1] += 1
        units[0] += 1


def loop_list(f, shelf_file):
    shelf = shelve.open(shelf_file)
    try:
        next_line = next(f)
        while next_line != '\n':
            build_list(shelf, [int(i) for i in next_line.split() if i.isdigit()])
            next_line = next(f)
    except StopIteration:
        print('end of file')

    shelf.close()


def define_lists():
    with open(input_file, 'r') as my_file:
        for line in my_file:
            if 'seeds:' in line:
                seeds = [int(i) for i in line.split() if i.isdigit()]
                print(f'seeds: {seeds}')

            if 'seed-to-soil' in line:
                loop_list(my_file, output_dir + "\\seed-to-soil")
                print('Completed seed_soil')

            if 'soil-to-fertilizer' in line:
                loop_list(my_file, output_dir + "\\soil-to-fertilizer")
                print('Completed soil_fert')

            if 'fertilizer-to-water' in line:
                loop_list(my_file, output_dir + "\\fertilizer-to-water")
                print('Completed fert_water')

            if 'water-to-light' in line:
                loop_list(my_file, output_dir + "\\water-to-light")
                print('Completed water_light')

            if 'light-to-temperature' in line:
                loop_list(my_file, output_dir + "\\light-to-temperature")
                print('Completed light_temp')

            if 'temperature-to-humidity' in line:
                loop_list(my_file, output_dir + "\\temperature-to-humidity")
                print('Completed temp_humidity')

            if 'humidity-to-location' in line:
                loop_list(my_file, output_dir + "\\humidity-to-location")
                print('Completed humidity_location')
    return seeds


def parse_info(data, info):
    dict_data = dict(list(data.values())[0])
    try:
        res = dict_data[info]
    except KeyError:
        res = info
    return res


def get_location(seed):
    with shelve.open(output_dir + "\\seed-to-soil") as my_file:
        if seed in my_file:
            soil = my_file[seed]
        else:
            soil = seed
#        soil = parse_info(my_file, seed)

    with shelve.open(output_dir + "\\soil-to-fertilizer") as my_file:
        fert = parse_info(my_file, soil)

    with shelve.open(output_dir + "\\fertilizer-to-water") as my_file:
        water = parse_info(my_file, fert)

    with shelve.open(output_dir + "\\water-to-light") as my_file:
        light = parse_info(my_file, water)

    with shelve.open(output_dir + "\\light-to-temperature") as my_file:
        temp = parse_info(my_file, light)

    with shelve.open(output_dir + "\\temperature-to-humidity") as my_file:
        humidity = parse_info(my_file, temp)

    with shelve.open(output_dir + "\\humidity-to-location") as my_file:
        loc = parse_info(my_file, humidity)

    return loc


my_cwd = os.getcwd()
if not os.path.isdir(my_cwd + "\\" + output_dir):
    print(f'Making directory: {output_dir}')
    os.mkdir(my_cwd + "\\" + output_dir)

seeds = define_lists()
lowest_location = -1
for seed in seeds:
    location = get_location(seed)
    print(f'The location for seed {seed} is {location}')
    if location < lowest_location or lowest_location == -1:
        lowest_location = location

print(f'\nThe lowest location is {lowest_location}')
