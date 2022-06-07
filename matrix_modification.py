def position_check(row, column):
    if 0 <= row <= rows - 1 and 0 <= column <= columns - 1:
        return True
    else:
        return False


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
columns = len(matrix[0])

while True:
    command = input().split()

    if command[0] == 'END':
        break

    order = command[0]
    row = int(command[1])
    column = int(command[2])
    number = int(command[3])
    is_valid = position_check(row, column)

    if not is_valid:
        print('Invalid coordinates')
        continue

    if order == 'Add':
        matrix[row][column] += number
    elif order == 'Subtract':
        matrix[row][column] -= number

for row in matrix:
    print(' '.join(str(x) for x in row))
