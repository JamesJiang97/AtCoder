H, W, rs, cs = map(int, input().split())
n = int(input())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))

q = int(input())

for i in range(q):
    d, l = map(input().split)
    l = int(l)
    if d =='L' :
        min = W
        for 