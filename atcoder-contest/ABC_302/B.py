h, w = map(int, input().split())
S = [input() for _ in range(h)]


# 定义8个可能的方向
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(matrix, word, x, y, pos, dx, dy):
    # 如果当前位置超出矩阵边界，或者当前位置的字母与目标单词对应位置的字母不同，返回失败
    if x<0 or y<0 or x>=len(matrix) or y>=len(matrix[0]) or matrix[x][y]!=word[pos]:
        return None

    # 如果找到的单词是目标单词的最后一个字母，返回当前位置
    if pos == len(word) - 1:
        return [(x+1, y+1)]  # 坐标为 1-indexed

    # 否则，继续向固定方向进行搜索
    result = dfs(matrix, word, x+dx, y+dy, pos+1, dx, dy)
    if result:
        return [(x+1, y+1)] + result  # 坐标为 1-indexed
    return None

def find_word(matrix, word):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for dx, dy in directions:
                result = dfs(matrix, word, i, j, 0, dx, dy)
                if result:
                    return result
    return None



# 用例测试
matrix = S

word = 'snuke'
result = find_word(matrix, word)

# 打印结果
for r in result:
    print(r[0], r[1])