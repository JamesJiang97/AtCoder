n, d = map(int, input().split())

X = []
Y = []
tag = [0] * n

tag[0] = 1

for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(n):
    for j in range(i+1, n):
        if (X[i] - X[j])**2 + (Y[i] - Y[j])**2 <= d**2:
            if tag[i] or tag[j]:
                tag[i] = 1
                tag[j] = 1

for i in range(n):
    if tag[i]:
        print("Yes")
    else:
        print("No")