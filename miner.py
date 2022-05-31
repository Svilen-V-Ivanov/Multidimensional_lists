def movement(order, row_position, column_position, n):
    if order == 'up':
        if row_position - 1 < 0:
            row_position = row_position
        else:
            row_position -= 1

    if order == 'down':
        if row_position + 1 > n - 1:
            row_position = row_position
        else:
            row_position += 1

    if order == 'left':
        if column_position - 1 < 0:
            column_position = column_position
        else:
            column_position -= 1

    if order == 'right':
        if column_position + 1 > n - 1:
            column_position = column_position
        else:
            column_position += 1

    return row_position, column_position


n = int(input())

matrix = []

commands = input().split()

for _ in range(n):
    matrix.append(input().split())

collected_coal = 0
coal_positions = []
miner_position = []
end_position = []
for row in range(n):
    for column in range(n):
        if matrix[row][column] == 's':
            miner_position = [row, column]
        elif matrix[row][column] == 'c':
            coal_position = [row, column]
            coal_positions.append(coal_position)
        elif matrix[row][column] == 'e':
            end_position = [row, column]

is_ended = False
is_collected = False
for order in commands:
    row_position = miner_position[0]
    column_position = miner_position[1]
    matrix[miner_position[0]][miner_position[1]] = '*'
    new_position = movement(order, row_position, column_position, n)
    miner_position = [new_position[0], new_position[1]]

    if miner_position in coal_positions:
        collected_coal += 1
        coal_positions.remove(miner_position)
        matrix[miner_position[0]][miner_position[1]] = '*'
    elif miner_position == end_position:
        print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
        is_ended = True
        break

    if not coal_positions:
        print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
        is_collected = True
        break

if not is_ended and not is_collected:
    print(f"{len(coal_positions)} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
