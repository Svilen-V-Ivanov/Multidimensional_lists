def movement(player_row, player_column, n, m):
    if order == 'U':
        return player_row -1, player_column
    if order == 'D':
        return player_row + 1, player_column
    if order == 'L':
        return player_row, player_column - 1
    if order == 'R':
        return player_row, player_column + 1


def is_outside(bunny_row, bunny_column, n, m):
    return bunny_row < 0 or bunny_column < 0 or bunny_row >= n or bunny_column >= m


def get_children(bunny_row, bunny_column, n, m):
    possible_children = [
        [bunny_row - 1, bunny_column],
        [bunny_row + 1, bunny_column],
        [bunny_row, bunny_column - 1],
        [bunny_row, bunny_column + 1]
    ]

    result = []
    for child_row, child_col in possible_children:
        if not is_outside(child_row, child_col, n, m):
            result.append([child_row, child_col])

    return result


n, m = (int(x) for x in input().split())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

commands = list(input())


bunny_positions = set()
player_row = 0
player_column = 0
for row in range(n):
    for column in range(m):
        if matrix[row][column] == 'P':
            player_row = row
            player_column = column
        elif matrix[row][column] == 'B':
            bunny_positions.add(f'{row} {column}')

is_dead = False
is_won = False
for order in commands:
    new_row, new_column = movement(player_row, player_column, n, m)
    matrix[player_row][player_column] = '.'

    if is_outside(new_row, new_column, n, m):
        is_won = True
    elif matrix[new_row][new_column] == 'B':
        is_dead = True
        player_row, player_column = new_row, new_column
    else:
        matrix[new_row][new_column] = 'P'
        player_row, player_column = new_row, new_column

    new_bunnies = set()
    for bunny in bunny_positions:
        bunny_row, bunny_column = [int(x) for x in bunny.split()]
        children = get_children(bunny_row, bunny_column, n, m)
        for child_row, child_col in children:
            new_bunnies.add(f'{child_row} {child_col}')
            matrix[child_row][child_col] = 'B'
            if child_row == player_row and child_col == player_column:
                is_dead = True

    bunny_positions = bunny_positions.union(new_bunnies)

    if is_won or is_dead:
        break

for row in matrix:
    print(''.join(row))

if is_won:
    print(f'won: {player_row} {player_column}')
else:
    print(f'dead: {player_row} {player_column}')