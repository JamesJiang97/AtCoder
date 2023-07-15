h, w = map(int, input().split())

S = [list(input()) for _ in range(h)]

def find_dot(matrix):
    S.insert(0, ['0'] * w)
    S.append(['0'] * w)
    for i in range(h+2):
        S[i].insert(0, '0')
        S[i].append('0')
    for i in range(1,h+1):
        for j in range(1,w+1):
            if matrix[i][j] == '.':
                if matrix[i][j+1] == '#' and matrix[i+1][j] == '#' and matrix[i+1][j+1] == '#':
                    return i, j
                elif matrix[i][j-1] == '#' and matrix[i+1][j] == '#' and matrix[i+1][j-1] == '#':
                    return i, j
                elif matrix[i][j+1] == '#' and matrix[i-1][j] == '#' and matrix[i-1][j+1] == '#':
                    return i, j
                elif matrix[i][j-1] == '#' and matrix[i-1][j] == '#' and matrix[i-1][j-1] == '#':
                    return i, j

i, j = find_dot(S)

print(str(i) + ' ' + str(j))