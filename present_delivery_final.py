def is_inside(next_row, next_column, rows):
    return 0 <= next_row < rows and 0 <= next_column < rows


def movement(santa_row, santa_column, command):
    movements = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1]
    }
    santa_row += movements[command][0]
    santa_column += movements[command][1]

    return santa_row, santa_column


gifts = int(input())
rows = int(input())

matrix = []
santa_row, santa_column = 0, 0
nice_children = 0
for row in range(rows):
    row_elements = input().split()
    for column in range(rows):
        if row_elements[column] == 'S':
            santa_row, santa_column = row, column
        elif row_elements[column] == 'V':
            nice_children += 1
    matrix.append(row_elements)

happy_nice_children = 0
while True:
    if gifts == 0:
        break
    command = input()

    if command == 'Christmas morning':
        break
    matrix[santa_row][santa_column] = '-'
    next_row, next_column = movement(santa_row, santa_column, command)
    if is_inside(next_row, next_column, rows):
        santa_row, santa_column = next_row, next_column

    if matrix[santa_row][santa_column] == 'V':
        gifts -= 1
        happy_nice_children += 1

    elif matrix[santa_row][santa_column] == 'C':
        next_children_list = ['left', 'right', 'up', 'down']
        for direction in next_children_list:
            child_row, child_col = movement(santa_row, santa_column, direction)
            if matrix[child_row][child_col] == 'X':
                gifts -= 1
            elif matrix[child_row][child_col] == 'V':
                gifts -= 1
                happy_nice_children += 1
            matrix[child_row][child_col] = '-'
            if gifts == 0:
                break

    matrix[santa_row][santa_column] = 'S'

if nice_children != happy_nice_children and gifts == 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(' '.join(row))

if nice_children == happy_nice_children:
    print(f"Good job, Santa! {happy_nice_children} happy nice kid/s.")
else:
    print(f"No presents for {nice_children - happy_nice_children} nice kid/s.")
