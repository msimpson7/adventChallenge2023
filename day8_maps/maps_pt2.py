import re

input_file = 'puzzle_input.txt'


def get_the_a(m):
    all_a = []
    for a_node in m:
        if re.search('..A', a_node):
            all_a.append(a_node)

    return all_a


def traverse_map(p, m):
    map_begin = get_the_a(m)
    print(f'map_begin is {map_begin}')
    # exit(0)
    c = 0
    j = 0
    while True:
        for s in p:
            update_map_begin = []
            for map_b in map_begin:
                map_b = m[map_b][0] if s == 'L' else m[map_b][1]
                update_map_begin.append(map_b)
            c += 1
            map_begin = update_map_begin

        done = True
        for map_b in map_begin:
            if not re.search('..Z', map_b):
                done = False
        if done:
            break
        if j % 100000 == 0:
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
