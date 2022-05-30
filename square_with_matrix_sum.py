import sys

n, m = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(n):
    matrix.append(input().split(', '))

max_sum = -sys.maxsize
max_matrix = []
for row in range(n - 1):
    for column in range(m - 1):
        current_sum = int(matrix[row][column]) + int(matrix[row + 1][column]) \
                      + int(matrix[row][column + 1]) + int(matrix[row + 1][column + 1])

        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = [[matrix[row][column], matrix[row][column + 1]],
                            [matrix[row + 1][column], matrix[row + 1][column + 1]]]

print(f"{max_matrix[0][0]} {max_matrix[0][1]}")
print(f"{max_matrix[1][0]} {max_matrix[1][1]}")
print(max_sum)