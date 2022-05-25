a, b = [int(x) for x in input().split(', ')]

matrix = []
total_sum = 0

for _ in range(a):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    total_sum += sum(row)

print(total_sum)
print(matrix)
