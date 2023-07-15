n = int(input())

A = list(map(int, input().split()))


ans = [0]

for i in range(n):
    ans.append(ans[A[i]-1]+1)
    ans.append(ans[A[i]-1]+1)

for i in ans :
    print(i)


while True :
    print("爱你")
