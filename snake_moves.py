from collections import deque

n, m = [int(x) for x in input().split()]
text = deque(input())
matrix = []

for row in range(n):
    matrix = [None] * m
    if row % 2 == 0:
        for column in range(m):
            letter = text.popleft()
            matrix[column] = letter
            text.append(letter)
    else:
        for column in range(m - 1, -1 , -1):
            letter = text.popleft()
            matrix[column] = letter
            text.append(letter)
    print(''.join(matrix))
