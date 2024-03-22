from datetime import datetime

input_file = 'puzzle_input.txt'


def build_list(info, units):
    if units[1] <= info <= units[1]+units[2]-1:
        return (info - units[1]) + units[0]
    return -1


def loop_list(data, info):
    res = -1
    for d in data:
        res = build_list(info, d)
        if not res == -1:
            break

    if res == -1:
        return info
    else:
        return res


def get_seeds():
    with open(input_file, 'r') as my_file:
        for line in my_file:
            if 'seeds:' in line:
                seed_list = [int(i) for i in line.split() if i.isdigit()]

    seedlings = seed_list[::2]
    seed_range = seed_list[1::2]
    return list(zip(seedlings, seed_range))


def get_location(seed):
    soil = loop_list(seed_to_soil, seed)
    fert = loop_list(soil_to_fert, soil)
    water = loop_list(fert_to_water, fert)
    light = loop_list(water_to_light, water)
    temp = loop_list(light_to_temp, light)
    humidity = loop_list(temp_to_humidity, temp)
    loc = loop_list(humidity_to_loc, humidity)

    return loc


def parse_file(data):
    output = []
    with open(input_file, 'r') as my_file:
        line = my_file.readline()
        while data not in line:
            line = my_file.readline()
        try:
            next_line = next(my_file)
            while next_line != '\n':
                output += [[int(i) for i in next_line.split() if i.isdigit()]]
                next_line = next(my_file)
        except StopIteration:
            pass
    return output


lowest_location = -1

seeds = get_seeds()
print(f'seeds: {seeds}')
seed_to_soil = parse_file('seed-to-soil')
soil_to_fert = parse_file('soil-to-fertilizer')
fert_to_water = parse_file('fertilizer-to-water')
water_to_light = parse_file('water-to-light')
light_to_temp = parse_file('light-to-temperature')
temp_to_humidity = parse_file('temperature-to-humidity')
humidity_to_loc = parse_file('humidity-to-location')

print(f'seed_to_soil: {seed_to_soil}\nsoil_to_fert: {soil_to_fert}\nfert_to_water: {fert_to_water}\n'
      f'water_to_light: {water_to_light}\nlight_to_temp: {light_to_temp}\n'
      f'temp_to_humidity: {temp_to_humidity}\nhumidity_to_location: {humidity_to_loc}')
count = 0
print('{} -- Completed {: 13,} iterations'.format(datetime.now().__format__('%Y-%m-%d %H:%M:%S %f'), count))
for seed in seeds:
    for i in range(seed[0], seed[0]+seed[1]):
        count += 1
        location = get_location(i)
        if location < lowest_location or lowest_location == -1:
            lowest_location = location
            print(f'location is now: {location}')
        if not count % 10000000:
            print('{} -- Completed {: 13,} iterations'.format(datetime.now().__format__('%Y-%m-%d %H:%M:%S %f'), count))

print(f'\nThe lowest location is {lowest_location}')
print(f'Number of seeds total was: {count:,}')
