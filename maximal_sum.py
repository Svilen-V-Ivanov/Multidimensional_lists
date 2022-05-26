n, m = [int(x) for x in input().split(' ')]

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(' ')])
max_sum = float('-inf')
start_row = 0
start_col = 0

for row in range(n - 2):
    for column in range(m - 2):
        current_sum = matrix[row][column] + matrix[row][column + 1] + matrix[row][column + 2] + \
                      matrix[row + 1][column] + matrix[row + 1][column + 1] + matrix[row + 1][column + 2] + \
                      matrix[row + 2][column] + matrix[row + 2][column + 1] + matrix[row + 2][column + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            start_row = row
            start_col = column

print(f"Sum = {max_sum}")
print(f"{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}")
print(f"{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} \
{matrix[start_row + 1][start_col + 2]}")
print(f"{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} \
{matrix[start_row + 2][start_col + 2]}")
