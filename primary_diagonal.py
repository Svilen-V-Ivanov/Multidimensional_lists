rows = int(input())

matrix = []
sum_main = 0

for _ in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

for row_index in range(rows):
    for column_index in range(rows):
        if row_index == column_index:
            sum_main += matrix[row_index][column_index]

print(sum_main)