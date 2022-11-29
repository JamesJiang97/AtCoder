import itertools

S = []

for i in range(9) :
    S.append(list(input()))

P = []

for r in range(9):
    for c in range(9):
        if S[r][c] == "#" :
            P.append([r,c])

c = itertools.combinations(P, 4)

ans = 0

for z in c :
    l = itertools.combinations(z, 2)
    
    for cp in l :
