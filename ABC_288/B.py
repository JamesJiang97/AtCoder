n, k =map(int,input().split())
S = []
for i in range(k):
    S.append(input())

S.sort()
for i in range(k):
    print(S[i])