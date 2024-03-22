
input_file = 'puzzle_input.txt'

with open(input_file, 'r') as my_file:
    data = my_file.readline()
    time = [int(i) for i in data.split() if i.isdigit()]
    data = my_file.readline()
    distance = [int(i) for i in data.split() if i.isdigit()]

print(f'Time is {time}\nDistance is {distance}')

time_concat = ''
for i in time:
    time_concat += str(i)
dist_concat = ''
for i in distance:
    dist_concat += str(i)

print(f'time_concat is {time_concat}\ndist_concat is {dist_concat}')


def win_chance(time, dist):
    win = 0
    for t in range(time+1):
        move = time - t
        if (t * move) > dist:
            win += 1

    return win


res = win_chance(int(time_concat), int(dist_concat))

print(f'Total wins = {res}')
