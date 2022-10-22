from itertools import combinations

n = int(input())

N = bin(n)[2:]

#N = N[::-1]

ini = ['0'] * len(N)


A = []

for i in range(len(N)-1, -1, -1):
    if N[i] == '1' : A.append(i+1)

#print(A)

q = len(A)

ans = []

for k in range(q+1):
    for comb in combinations(A, k):
        #print(comb)
        t = ['0'] * len(N)
        #print(t)
        for i in comb :
            t[i-1] = '1'
        st = "".join(t)
        #print(st)
        ans.append(int(st, 2))

ans.sort()

for i in ans :
    print(i)
