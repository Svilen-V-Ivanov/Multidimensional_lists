def optimal_path(bunny_row, bunny_column, rows):
    direction = ''
    sums = {
        'up': 0,
        'down': 0,
        'left': 0,
        'right': 0
    }
    paths = {
        'up': [],
        'down': [],
        'left': [],
        'right': []
    }
    if bunny_row != 0:
        for up in range(bunny_row - 1, -1, -1):
            current_position = matrix[up][bunny_column]
            if current_position != 'X':
                sums['up'] += int(current_position)
                paths['up'].append(f"{up}, {bunny_column}")
            else:
                break

    if bunny_row != rows - 1:
        for down in range(bunny_row + 1, rows):
            current_position = matrix[down][bunny_column]
            if current_position != 'X':
                sums['down'] += int(current_position)
                paths['down'].append(f"{down}, {bunny_column}")
            else:
                break

    if bunny_column != 0:
        for left in range(bunny_column - 1, -1, -1):
            current_position = matrix[bunny_row][left]
            if current_position != 'X':
                sums['left'] += int(current_position)
                paths['left'].append(f"{bunny_row}, {left}")
            else:
                break

    if bunny_column != rows - 1:
        for right in range(bunny_column + 1, rows):
            current_position = matrix[bunny_row][right]
            if current_position != 'X':
                sums['right'] += int(current_position)
                paths['right'].append(f"{bunny_row}, {right}")
            else:
                break

    new_dict = {
        'up': [sums['up'], paths['up']],
        'down': [sums['down'], paths['down']],
        'left': [sums['left'], paths['left']],
        'right': [sums['right'], paths['right']],
    }
    sorted_dict = sorted(new_dict.items(), key=lambda x: (-x[1][0], -len(x[0][1])))
    final_list = []
    for tuple in range(len(sorted_dict)):
        if sorted_dict[tuple][1][0] != 0 or sorted_dict[tuple][1][1]:
            final_list.append(sorted_dict[tuple])
    key = final_list[0][0]
    value = final_list[0][1][0]
    list = final_list[0][1][1]
    return key, list, value


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append(input().split())

bunny_row = 0
bunny_column = 0
sum_eggs = 0
for row in range(rows):
    for column in range(rows):
        if matrix[row][column] == 'B':
            bunny_row = row
            bunny_column = column

direction, bunny_path, sum_eggs = optimal_path(bunny_row, bunny_column, rows)

print(direction)
for egg in bunny_path:
    key, value = egg.split(', ')
    print(f"[{key}, {value}]")
print(sum_eggs)
