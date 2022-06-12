def is_outside(next_row, next_column, rows):
    return next_row < 0 or next_column < 0 or next_row >= rows or next_column >= rows


def movement(alice_row, alice_column, action):
    movements = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1]
    }
    alice_row += movements[action][0]
    alice_column += movements[action][1]

    return alice_row, alice_column


rows = int(input())

matrix = []
tea_list = '012345678910'
alice_row, alice_column = 0, 0
hole_row, hole_column = 0, 0
tea_positions = []
for row in range(rows):
    row_elements = input().split()
    for column in range(rows):
        if row_elements[column] == 'A':
            alice_row, alice_column = row, column
        elif row_elements[column] == 'R':
            hole_row, hole_column = row, column
        elif row_elements[column] in tea_list:
            tea_positions.append(f"{row} {column}")
    matrix.append(row_elements)

is_won = False
is_out = False
collected_tea = 0
while True:
    action = input()
    next_row, next_column = movement(alice_row, alice_column, action)
    matrix[alice_row][alice_column] = '*'

    if is_outside(next_row, next_column, rows):
        is_out = True
        break
    elif f"{next_row} {next_column}" in tea_positions:
        collected_tea += int(matrix[next_row][next_column])
        tea_positions.remove(f"{next_row} {next_column}")
        alice_row, alice_column = next_row, next_column

        if collected_tea >= 10:
            is_won = True
            matrix[alice_row][alice_column] = '*'
            break
        else:
            matrix[alice_row][alice_column] = 'A'
    elif next_row == hole_row and next_column == hole_column:
        alice_row, alice_column = next_row, next_column
        matrix[alice_row][alice_column] = '*'
        is_out = True
        break
    else:
        alice_row, alice_column = next_row, next_column
        matrix[alice_row][alice_column] = 'A'

if is_out:
    print("Alice didn't make it to the tea party.")
if is_won:
    print("She did it! She went to the party.")
for row in matrix:
    print(' '.join(row))
