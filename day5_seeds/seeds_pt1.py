input_file = 'puzzle_input.txt'


def build_list(list_builder, units):
    for i in range(units[2]):
        list_builder.append((units[1], units[0]))
        units[1] += 1
        units[0] += 1

    return list_builder


def loop_list(list_def, f):
    try:
        next_line = next(f)
        while next_line != '\n':
            build_list(list_def, [int(i) for i in next_line.split() if i.isdigit()])
            next_line = next(f)
    except StopIteration:
        print('end of file')


def define_lists():
    with open(input_file, 'r') as my_file:
        for line in my_file:
            if 'seeds:' in line:
                seeds = [int(i) for i in line.split() if i.isdigit()]
                print(f'seeds: {seeds}')

            if 'seed-to-soil' in line:
                loop_list(seed_soil, my_file)
                print(f'seed_soil: {seed_soil}')

            if 'soil-to-fertilizer' in line:
                loop_list(soil_fert, my_file)
                print(f'soil_fert: {soil_fert}')

            if 'fertilizer-to-water' in line:
                loop_list(fert_water, my_file)
                print(f'fert_water: {fert_water}')

            if 'water-to-light' in line:
                loop_list(water_light, my_file)
                print(f'water_light: {water_light}')

            if 'light-to-temperature' in line:
                loop_list(light_temp, my_file)
                print(f'light_temp: {light_temp}')

            if 'temperature-to-humidity' in line:
                loop_list(temp_humidity, my_file)
                print(f'temp_humidity: {temp_humidity}')

            if 'humidity-to-location' in line:
                loop_list(humidity_location, my_file)
                print(f'humidity_location: {humidity_location}')
    return seeds


def get_location(seed):
    dict_soil = dict(seed_soil)
    try:
        soil = dict_soil[seed]
    except KeyError:
        soil = seed
#    print(f'soil is {soil}')

    dict_fert = dict(soil_fert)
    try:
        fert = dict_fert[soil]
    except KeyError:
        fert = soil
#    print(f'fert is {fert}')

    dict_water = dict(fert_water)
    try:
        water = dict_water[fert]
    except KeyError:
        water = fert
#    print(f'water is {water}')

    dict_light = dict(water_light)
    try:
        light = dict_light[water]
    except KeyError:
        light = water
#    print(f'light is {light}')

    dict_temp = dict(light_temp)
    try:
        temp = dict_temp[light]
    except KeyError:
        temp = light
#    print(f'temp is {temp}')

    dict_humidity = dict(temp_humidity)
    try:
        humidity = dict_humidity[temp]
    except KeyError:
        humidity = temp
#    print(f'humidity is {humidity}')

    dict_location = dict(humidity_location)
    try:
        loc = dict_location[humidity]
    except KeyError:
        loc = humidity
#    print(f'loc is {loc}')

    return loc

# try:
#     with open(input_file, 'r') as my_file:
#         file_info = my_file.readlines()
# except FileNotFoundError as e:
#     print(f'Could not find file -- {e}')

# We want to pull in the "text1_text0 list
# And loop until a blank line with data1, data0, data2
# Build list with the values


seed_soil = []
soil_fert = []
fert_water = []
water_light = []
light_temp = []
temp_humidity = []
humidity_location = []
lowest_location = -1

seeds = define_lists()
for seed in seeds:
    location = get_location(seed)
    print(f'The location for seed {seed} is {location}')
    if location < lowest_location or lowest_location == -1:
        lowest_location = location

print(f'\nThe lowest location is {lowest_location}')
