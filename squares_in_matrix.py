n, m = [int(x) for x in input().split(' ')]

matrix = []

for _ in range(n):
    matrix.append(input().split())

squares = 0

for row in range(n - 1):
    for col in range(m - 1):
        if matrix[row][col] == matrix[row + 1][col] == matrix[row][col + 1] == matrix[row + 1][col + 1]:
            squares += 1

print(squares)
