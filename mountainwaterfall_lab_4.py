def gridmaker(str, strlen, grid, row):
    for i in range(strlen):
        if str[i] == 'o':
            grid[row][i] = 'o'
        elif str[i] == '*':
            grid[row][i] = '*'
        elif str[i] == '.':
            grid[row][i] = '.'

def checker(grid, row, col, length, depth):
    grid[row][col] = '*'
    if row + 1 < depth and grid[row + 1][col] != 'o' and grid[row + 1][col] != '*':
        checker(grid, row + 1, col, length, depth)
    elif row + 1 < depth and grid[row + 1][col] == 'o':
        if col + 1 < length and grid[row][col + 1] == '.':
            checker(grid, row, col + 1, length, depth)
        if col - 1 >= 0 and grid[row][col - 1] == '.':
            checker(grid, row, col - 1, length, depth)

depth, length = input().split()
depth = int(depth)
length = int(length)
grid = [['.' for _ in range(length)] for _ in range(depth)]

for i in range(depth):
    row_str = input().strip()
    gridmaker(row_str, length, grid, i)

for i in range(depth):
    for j in range(length):
        if grid[i][j] == '*':
            checker(grid, i, j, length, depth)

for row in grid:
    print(''.join(row))

