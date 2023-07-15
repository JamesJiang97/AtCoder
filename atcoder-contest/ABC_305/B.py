# 创建一个字典来存储每个字母的位置
positions = {
    'A': 0,
    'B': 3,
    'C': 4,
    'D': 8,
    'E': 9,
    'F': 14,
    'G': 23
}

def distance(letter1, letter2):
    # 计算并返回两个字母之间的距离
    return abs(positions[letter1] - positions[letter2])

p, q = input().split()

# 测试这个函数
print(distance(p, q))
