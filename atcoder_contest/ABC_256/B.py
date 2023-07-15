n = int(input())
A = list(map(int, input().split()))

masu = [0] * 4
P = 0

for i in range(len(A)) :
    a = A[i]
    masu[0] = 1
    for j in range(3, -1, -1) :
        if masu[j] == 0 :
            continue
        else :
            if j + A[i] > 3 :
                masu[j] = 0
                P += 1
            else :
                masu [j] = 0
                masu [j+A[i]] = 1

print(P)