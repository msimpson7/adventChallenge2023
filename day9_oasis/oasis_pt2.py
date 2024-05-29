input_file = 'puzzle_input.txt'


def get_val(s):
    # split the line
    vals = s.split()
    print(vals)
    diffs = []
    fin = [int(vals[0])]
    for v in range(len(vals)-1):
        diffs.append(int(vals[v+1])-int(vals[v]))
    print(diffs)
    fin.append(diffs[0])
    while sum(diffs) != 0:
        new_diffs = diffs
        diffs = []
        for v in range(len(new_diffs)-1):
            diffs.append(new_diffs[v+1]-new_diffs[v])
        print(diffs)
        fin.append(diffs[0])

    val = 0
    for v in reversed(range(len(fin))):
        val = fin[v] - val

    print(val)
    return val


his = 0
with open(input_file, 'r') as file:
    line = file.readline().strip()
    while True:
        if not line:
            break
        his += get_val(line)
        print("\n")
        line = file.readline().strip()

print(f'The final value is {his}')
