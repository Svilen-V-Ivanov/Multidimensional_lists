size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(', ')])
primary = []
secondary = []

for prim in range(size):
    primary.append(matrix[prim][prim])
    secondary.append(matrix[prim][size - 1 - prim])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
