n = int(input())

A = [0]

for i in range(n) :
    A.append(int(input()))

lighting = 1

ans = -1

for i in range(n) :
    lighting = A[lighting]
    if lighting == 2 :
        ans = i + 1
        break

print(ans)