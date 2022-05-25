n, m = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(' ')])

column_sums = [0] * m

for row_index in range(n):
    for column_index in range(m):
        column_sums[column_index] += matrix[row_index][column_index]

[print(x) for x in column_sums]