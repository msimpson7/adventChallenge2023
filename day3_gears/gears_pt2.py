import math

input_file = 'play_puzzle_input.txt'

# We want the sum of the products of numbers around a '*'
# when there are exactly 2 numbers surrounding it

try:
    with open(input_file, 'r') as my_file:
        file_info = my_file.readlines()
except FileNotFoundError as e:
    print(f'Could not find file -- {e}')

summation = 0
total_rows = len(file_info)
total_cols = len(file_info[0])-1


def calculate_number(grid, index, j):
    current_end = j
    while j > 0 and grid[index][j].isdigit():
        j -= 1
    if j == 0 and grid[index][j].isdigit():
        current_beg = j
    else:
        current_beg = j+1

    j = current_end
    while j < total_cols and grid[index][j].isdigit():
        j += 1
    if j == total_cols and grid[index][j].isdigit():
        current_end = j+1
    else:
        current_end = j

    num_str = grid[index][current_beg:current_end]
    num = int(num_str)
    print(num)

    str = ''
    for j in range(current_beg, current_end):
        str += '.'

    if current_beg > 0 and current_end < total_cols:
        str = grid[index][current_beg - 1] + str + grid[index][current_end]
        num_str = grid[index][current_beg - 1] + num_str + grid[index][current_end]
    elif current_beg > 0:
        str = grid[index][current_beg - 1] + str
        num_str = grid[index][current_beg - 1] + num_str
    else:
        str = str + grid[index][current_end]
        num_str = num_str + grid[index][current_end]

    print(f'******** ROW {index} ********')
    print(grid[index])
    print(f'{num_str}\n{str}')
    grid[index] = grid[index].replace(num_str, str)
    print(grid[index])

    return num


def get_number_near(grid, i, j):
    prod = []
    if j > 0:
        if grid[i][j-1].isdigit():
            num = calculate_number(grid, i, j-1)
            if num > 0:
                print(f'Added {num}')
                prod.append(num)
                print(f'length of prod is {len(prod)}')

    if i > 0 and j > 0:
        if grid[i-1][j-1].isdigit():
            num = calculate_number(grid, i-1, j-1)
            if num > 0:
                print(f'Added {num}')
                prod.append(num)
                print(f'length of prod is {len(prod)}')

    if i > 0:
        if grid[i-1][j].isdigit():
            num = calculate_number(grid, i-1, j)
            if num > 0:
                print(f'Added {num}')
                prod.append(num)
                print(f'length of prod is {len(prod)}')

    if i > 0 and j < total_cols:
        if grid[i-1][j+1].isdigit():
            num = calculate_number(grid, i-1, j+1)
            if num > 0:
                print(f'Added {num}')
                prod.append(num)
                print(f'length of prod is {len(prod)}')

    if j < total_cols:
        if grid[i][j+1].isdigit():
            num = calculate_number(grid, i, j+1)
            if num > 0:
                print(f'Added {num}')
                prod.append(num)
                print(f'length of prod is {len(prod)}')

    if i < total_rows and j < total_cols:
        if grid[i+1][j+1].isdigit():
            num = calculate_number(grid, i+1, j+1)
            if num > 0:
                print(f'Added {num}')
                prod.append(num)
                print(f'length of prod is {len(prod)}')

    if i < total_rows:
        if grid[i+1][j].isdigit():
            num = calculate_number(grid, i+1, j)
            if num > 0:
                print(f'Added {num}')
                prod.append(num)
                print(f'length of prod is {len(prod)}')

    if i < total_rows and j > 0:
        if grid[i+1][j-1].isdigit():
            num = calculate_number(grid, i+1, j-1)
            if num > 0:
                print(f'Added {num}')
                prod.append(num)
                print(f'length of prod is {len(prod)}')

    if len(prod) == 2:
        print(f'There are 2 numbers: {prod} Their product is {math.prod(prod)}')
        return math.prod(prod)
    else:
        return 0


symbols = ['*']

try:
    for row in range(total_rows):
        for col in range(total_cols):
            if file_info[row][col] in symbols:
                num = get_number_near(file_info, row, col)
                summation += num
except IndexError as e:
    print(f"The error occurred when row was {row} and col was {col} -- {e}")

print(f"The sum of the numbers is {summation}")

