n = int(input())

A = list(map(int, input().split()))

list.sort(A, reverse=True)

temp = []

count = 0

for i in range(n):
    if len(temp)==0 or temp[-1][0] != A[i] :
        icnt = 1
        temp.append([A[i], icnt, count])
        count += 1
    else:
        temp[-1][1] +=1

max = len(temp) - 1

for i in range(n):
    if i <= max:
        print(temp[i][1])
    else: print(0)
