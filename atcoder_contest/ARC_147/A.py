n = int(input())

A = list(map(int, input().split()))

A.sort()

cnt = 0

max = n - 1

while(max +1 > 1) :
    #print(A)
    cnt += 1
    A[max] = A[max] % A[0]
    if A[max] == 0 :
        max -= 1
        continue
    if max + 1 == 1 : break
    insi = A.pop(max)
    A.insert(0, insi)

print(cnt)

