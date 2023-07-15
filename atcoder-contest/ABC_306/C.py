n = int(input())

A = list(map(int, input().split()))

tag = [0]*(n+1)

dict = {}

for i in range(3*n):
    tag[A[i]] += 1
    if tag[A[i]] == 2:
        dict[A[i]] = i+1


dict1 = sorted(dict.items(), key=lambda x:x[1])


for i in dict1:
    print(i[0], end=' ')
