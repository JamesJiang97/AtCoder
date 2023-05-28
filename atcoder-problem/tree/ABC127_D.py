import heapq


n, m = map(int, input().split())

A = list(map(int, input().split()))

BC = []

for z in range(m) : 
    bc = list(map(int, input().split()))
    BC.append(bc)

BC = sorted(BC, reverse=True, key=lambda x: x[1])

heapq.heapify(A)

for i in range(m) :
    b = BC[i][0]
    c = BC[i][1] 
    if c <= A[0] :
        continue
    else :
        for z in range(b) :
            heapq.heapreplace(A, c)
            if c <= A[0] : continue
    
print(sum(A))


