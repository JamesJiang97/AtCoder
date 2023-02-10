n, t = map(int, input().split())

A = list(map(int, input().split()))

r = sum(A)

now = t % r

for i in range(n):
    now -= A[i]
    if now < 0 : 
        print(str(i+1) + " " + str(now+A[i]))
        break