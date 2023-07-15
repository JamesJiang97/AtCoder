

h, w = map(int, input().split())

A = []
for i in range(h) :
    A.append(list(map(int, input().split())))

B = [[0 for i in range(w)] for j in range(h)]

sumH = []
sumW = []

for i in range(h) :
    sumH.append(sum(A[i]))

for j in range(w) :
    sum = 0
    for i in range(h) :
        sum += A[i][j]
    sumW.append(sum)

for i in range(h) :
    for j in range(w) :
        B[i][j] = sumH[i] + sumW[j] - A[i][j]

for i in range(h) : 
    print(*B[i], sep = " ")
