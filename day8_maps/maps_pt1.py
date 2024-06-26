input_file = 'puzzle_input.txt'


def traverse_map(p, m):
    map_begin = 'AAA'
    map_end = 'ZZZ'
    c = 0
    j = 0
    while True:
        for s in p:
            map_begin = m[map_begin][0] if s == 'L' else m[map_begin][1]
            c += 1

        if map_begin == map_end:
            break
        print(f'Iteration #{j}')
        j += 1

    return c


maps = {}
with open(input_file, 'r') as file:
    path = file.readline().strip()
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        node, network = line.split(' = ')
        maps[node] = network.strip().replace('(', '').replace(')', '').split(', ')

print(f'path is {path}')
print(f'maps is {maps}')

count = traverse_map(path, maps)
print(f'count is {count}')
