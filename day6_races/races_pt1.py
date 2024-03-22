
input_file = 'puzzle_input.txt'

with open(input_file, 'r') as my_file:
    data = my_file.readline()
    time = [int(i) for i in data.split() if i.isdigit()]
    data = my_file.readline()
    distance = [int(i) for i in data.split() if i.isdigit()]

print(f'Time is {time}')
print(f'Distance is {distance}')


def win_chance(time, dist):
    win = 0
    for t in range(time+1):
        move = time - t
        if (t * move) > dist:
            win += 1

    print(f'time {time} = {win} wins')
    return win


res = 1
for i in range(len(time)):
    res *= win_chance(time[i], distance[i])

print(f'Total wins = {res}')
