n = int(input())

A = list(map(int,input().split()))

ans = []

for i in range(n):
    start = i*7
    end = start + 7
    sum_num = 0
    for j in range(start,end):
        sum_num += A[j]
    ans.append(sum_num)

for i in ans:
    print(i ,end=" ")