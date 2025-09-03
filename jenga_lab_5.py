'''
TODO LIST:
- adjust for suboptimal first row rather than greedy first row
- make printer function to print everything
'''






def calculator(rows, cols, bricklength, weights):   # weights is a list of lists for rows and cols weights
    max_val = -1
    indexes = []
    current_idx = -1

    # first row
    if weights[0][0] > max_val:
        current_val = 0
    for k in range(cols - bricklength):
        if k == 0:
            for l in range(bricklength):
                current_val += weights[0][l]
            if current_val > max_val:
                max_val = current_val
                current_idx = 0
        else:
            current_val -= weights[0][k-1]
            current_val += weights[0][bricklength + k]
            if current_val > max_val:
                current_idx = k
    indexes.append(current_idx)

    # rest of the rows
    for i in range(1, rows):
        for j in range(max(0, (current_idx - bricklength + 1)), min((current_idx + bricklength - 1), cols)):
            row_val = 0
            if j == (max(0, (current_idx - bricklength + 1))):
                for m in range(bricklength):
                    row_val += weights[i][m]
                if row_val + current_val > max_val:
                    max_val = row_val + current_val
                    indexes.append(max(0, (current_idx - bricklength + 1)))
            else:
                row_val -= weights[i][j-1]
                row_val += weights[i][bricklength + j]
                if row_val + current_val > max_val:
                    max_val = row_val + current_val
                    indexes[i] = j

    return indexes

def printer(rows, cols, bricklength, indexes):
