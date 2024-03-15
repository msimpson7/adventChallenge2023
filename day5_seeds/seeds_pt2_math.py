input_file = 'puzzle_input.txt'


def build_list(info, units):
    if units[1] <= info <= units[1]+units[2]-1:
        return (info - units[1]) + units[0]
    return -1


def loop_list(f, info):
    res = -1
    try:
        next_line = next(f)
        while res == -1 and next_line != '\n':
            res = build_list(info, [int(i) for i in next_line.split() if i.isdigit()])
            next_line = next(f)
    except StopIteration:
        pass

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


def get_info(loc, info):
    with open(input_file, 'r') as my_file:
        line = my_file.readline()
        while loc not in line:
            line = my_file.readline()
        res = loop_list(my_file, info)

    return res


def get_location(seed):
    soil = get_info('seed-to-soil', seed)
    fert = get_info('soil-to-fertilizer', soil)
    water = get_info('fertilizer-to-water', fert)
    light = get_info('water-to-light', water)
    temp = get_info('light-to-temperature', light)
    humidity = get_info('temperature-to-humidity', temp)
    loc = get_info('humidity-to-location', humidity)

    return loc


lowest_location = -1

seeds = get_seeds()
print(f'seeds: {seeds}')
count = 0
for seed in seeds:
    for i in range(seed[0], seed[0]+seed[1]):
        count += 1
        location = get_location(i)
        print(f'The location for seed {i} is {location}')
        if location < lowest_location or lowest_location == -1:
            lowest_location = location

print(f'\nThe lowest location is {lowest_location}')
print(f"Numer of seeds total was: {count}")
