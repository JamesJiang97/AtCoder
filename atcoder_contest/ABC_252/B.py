N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

tag = [0]
max = 0
for i in range(N) :
    if A[i] > max :
        max = A[i]
        tag.clear()
        tag.append(i+1)
    if A[i] == max :
        tag.append(i+1)

for i in B : 
    if i in tag : 
        print('Yes')
        break
else : print('No')