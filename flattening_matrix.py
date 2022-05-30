rows = int(input())
matrix = [map(int, input().split(', ')) for _ in range(rows)]
flat = [num for row in matrix for num in row]
print(flat)