n = int(input())

S = []
A = []

for _ in range(n):
    s, a = input().split()
    S.append(s)
    A.append(int(a))

start = A.index(min(A))

for i in range(n):
    idex = i+start
    print(S[idex%n])
