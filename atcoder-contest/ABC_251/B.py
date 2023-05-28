from posixpath import split


N, W = map(int, input().split())
A = list(map(int, input().split()))
count = 0
flag = []
for i in range(W + 1) : flag.append(0)

for i in range(N) : 
    if A[i] <= W : flag[A[i]] = 1
    for j in range(i+1, N) : 
        res = A[i] + A[j]
        if res <= W : flag[res] = 1
        for k in range(j+1, N):
            res = A[i] + A[j] + A[k]
            if res <= W : flag[res] = 1

for i in flag : 
    count += i;

print(count)
