numbers = input().split('|')
matrix = []
for num in range(len(numbers) - 1, -1, -1):
    current_set = numbers[num].split()
    matrix.append(current_set)

flattened_matrix = [num for sublist in matrix for num in sublist]
print(' '.join(str(x) for x in flattened_matrix))
