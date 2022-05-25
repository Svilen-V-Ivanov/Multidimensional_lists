rows = int(input())

square_matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    square_matrix.append([x for x in row if x % 2 == 0])

print(square_matrix)


