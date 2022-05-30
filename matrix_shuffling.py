def check(row, col, n, m):
    return row < 0 or col < 0 or row >=n or col >= m


n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    matrix.append(input().split(' '))

while True:
    command = input().split()

    if command[0] == 'END':
        break
    if len(command) != 5 or command[0] != 'swap':
        print('Invalid input!')
        continue

    row_1, col_1, row_2, col_2 = [int(x) for x in command[1:]]

    if check(row_1, col_1, n, m) or check(row_2, col_2, n, m):
        print('Invalid input!')
        continue

    matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]

    for row in matrix:
        print(*row, sep=' ')