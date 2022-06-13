def is_inside(next_row, next_column, rows):
    return 0 <= next_row < rows and 0 <= next_column < rows


def movement(player_row, player_column, direction, distance):
    movements = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1]
    }
    player_row += movements[direction][0] * distance
    player_column += movements[direction][1] * distance

    return player_row, player_column


rows = 5

matrix = []
all_targets = 0
player_row, player_column = 0, 0
for row in range(rows):
    row_elements = input().split()
    for column in range(rows):
        if row_elements[column] == 'A':
            player_row, player_column = row, column
        elif row_elements[column] == 'x':
            all_targets += 1
    matrix.append(row_elements)

commands = int(input())
targets_hit = []
shot_targets = 0
matrix[player_row][player_column] = '.'

for _ in range(commands):
    order = input().split()
    action = order[0]
    direction = order[1]
    if action == 'move':
        distance = int(order[2])
        next_row, next_column = movement(player_row, player_column, direction, distance)

        if is_inside(next_row, next_column, rows) and matrix[next_row][next_column] == '.':
            player_row, player_column = next_row, next_column

    else:
        bullet_row, bullet_column = movement(player_row, player_column, direction, 1)

        while is_inside(bullet_row, bullet_column, rows):
            if matrix[bullet_row][bullet_column] == 'x':
                all_targets -= 1
                matrix[bullet_row][bullet_column] = '.'
                targets_hit.append([bullet_row, bullet_column])
                break
            bullet_row, bullet_column = movement(bullet_row, bullet_column, direction, 1)

        if all_targets == 0:
            break

if all_targets == 0:
    print(f"Training completed! All {len(targets_hit)} targets hit.")
else:
    print(f"Training not completed! {all_targets} targets left.")

print(*targets_hit, sep='\n')
