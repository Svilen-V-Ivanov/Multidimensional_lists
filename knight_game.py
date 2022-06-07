def is_outside(k_row, k_column, rows):
    return k_row < 0 or k_column < 0 or k_row >= rows or k_column >= rows


def get_movements(knight_row, knight_column, rows):
    possible_movements = [
        [knight_row - 1, knight_column - 2],
        [knight_row - 1, knight_column + 2],
        [knight_row - 2, knight_column - 1],
        [knight_row - 2, knight_column + 1],
        [knight_row + 1, knight_column - 2],
        [knight_row + 1, knight_column + 2],
        [knight_row + 2, knight_column - 1],
        [knight_row + 2, knight_column + 1],
    ]
    result = []
    for k_row, k_column in possible_movements:
        if not is_outside(k_row, k_column, rows):
            result.append([k_row, k_column])

    return result


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))
is_done = False
to_remove = 0
while True:

    if is_done:
        break

    knight_positions = []
    for row in range(rows):
        for column in range(rows):
            if matrix[row][column] == 'K':
                knight_positions.append(f'{row} {column}')

    max_counter = - float('inf')
    max_row, max_col = 0, 0
    for knight in knight_positions:
        knight_row, knight_column = [int(x) for x in knight.split()]
        movement = get_movements(knight_row, knight_column, rows)
        counter = 0
        for move in movement:
            move_row, move_column = int(move[0]), int(move[1])
            to_move = f'{move_row} {move_column}'
            if to_move in knight_positions:
                counter += 1

        if counter > max_counter:
            max_counter = counter
            max_row, max_col = knight_row, knight_column

    if max_counter != 0:
        matrix[max_row][max_col] = '0'
        to_remove += 1
    else:
        is_done = True

print(to_remove)
