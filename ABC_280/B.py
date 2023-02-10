n = int(input())
S = list(map(int, input().split()))

A = [S[0]]

for i in range(1, n):
    A.append(S[i]-S[i-1])

for a in A :
    print(str(a), end = ' ')