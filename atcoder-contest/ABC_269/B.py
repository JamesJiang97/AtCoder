S = [input() for l in range(10)]


A = -1
B = -1
C = -1
D = -1
fA = 0
fB = 0
fC = 0
fD = 0

for i in range(10):
    for j in range(10):
        if S[i][j] == '#' and fA == 0 and fB == 0 :
            A = i + 1
            C = j + 1
            fA = 1
            fC = 1
        if i == A - 1 and S[i][j] == '.' and fD == 0:
            D = j
            fD = 1
        if i == A - 1 and j == 9 and S[i][j] == '#' and fD == 0:
            D = 10
            fD = 1
        if S[i][j] == '.' and j == C - 1 and fB == 0: 
            B = i
            fB = 1
        if j == C - 1 and i == 9 and S[i][j] == '#' and fB == 0:
            B = 10
            fB = 1

print(str(A) + ' ' + str(B))
print(str(C) + ' ' + str(D))
