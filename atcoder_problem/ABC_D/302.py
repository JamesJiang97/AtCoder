# Category: D - Kyu in AtCoder

n, m, d = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()



while m > 0 and n > 0:
    if abs(A[-1]-B[-1]) <= d:
        print(A[-1]+B[-1])
        exit()
    else:
        if A[-1] > B[-1]:
            A.pop()
            n -= 1
        else:
            B.pop()
            m -= 1

print(-1)


