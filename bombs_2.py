def valid(row, column, n):
    children = []
    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            if n > r >= 0 and n > c >= 0:
                children.append([r, c])

    return children


n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

locations = input().split()

for bomb in locations:
    row, column = [int(x) for x in bomb.split(',')]
    power = matrix[row][column]

    if power <= 0:
        continue

    children = valid(row, column, n)

    for child_row, child_column in children:
        if matrix[child_row][child_column] <= 0:
            continue
        else:
            matrix[child_row][child_column] -= power

alive_cells = 0
sum = 0

for row in matrix:
    for num in row:
        if num > 0:
            alive_cells += 1
            sum += num

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum}")
for row in matrix:
    print(*row, sep=' ')