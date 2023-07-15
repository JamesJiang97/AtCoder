def print_outer(matrix, n):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return

    top = 0
    bottom = n-1
    left = 0
    right = n-1

    # Print top row from left to right
    for j in range(left, right + 1):
        
        if j == 0:
            temp = matrix[top][j]
            matrix[top][j] = matrix[1][0]
        else:
            cur = temp
            temp = matrix[top][j]
            matrix[top][j] = cur

    # Print right column from top to bottom
    for i in range(top + 1, bottom):
        cur = temp
        temp = matrix[i][right]
        matrix[i][right] = cur
        # print(matrix[i][right], end=' ')

    # Print bottom row from right to left
    if bottom > top:
        for j in range(right, left - 1, -1):
            cur = temp
            temp = matrix[bottom][j]
            matrix[bottom][j] = cur
            # print(matrix[bottom][j], end=' ')

    # Print left column from bottom to top
    if right > left:
        for i in range(bottom - 1, top, -1):
            cur = temp
            temp = matrix[i][left]
            matrix[i][left] = cur
            # print(matrix[i][left], end=' ')


n = int(input())
matrix = [list(input()) for _ in range(n)]

# Test the function

print_outer(matrix, n)

for row in matrix:
    print("".join(map(str, row)))
