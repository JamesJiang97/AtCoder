n = int(input())

A = list(map(int, input().split()))

ans = []

for i in range(n):
    if i == n-1:
        ans.append(A[i])
        break
    else:
        ans.append(A[i])
        if A[i] < A[i+1]:
            for j in range(1, A[i+1]-A[i]):
                ans.append(A[i]+j)
        elif A[i] > A[i+1]:
            for j in range(1, A[i]-A[i+1]):
                ans.append(A[i]-j)

for i in ans:
    print(i)
    

