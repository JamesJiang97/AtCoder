n, k = map(int, input().split())

T = list(map(int, input().split()))

A = [0] + T


tag = 1

for i in range(1, n-k+1) :
    if A[i] > A[i+k] :
        A[i], A[i+k] = A[i+k], A[i]
    if A[i] < A[i-1] :
        tag = 0
        break

for i in range(2, n+1) :
    if A[i] < A[i-1] :
        tag = 0
        break

if tag : print("Yes")
else : print("No")