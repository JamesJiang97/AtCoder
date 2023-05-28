n = int(input())
A = [list(str(input())) for i in range(n)]


ans = []

for i in range(n) :
    for j in range(n) :
        for t in range(n) :
            up = []
            down = []
            
            ti = i - t
            up.append(A[ti][j])
            ans.append(int(''.join(up)))
        