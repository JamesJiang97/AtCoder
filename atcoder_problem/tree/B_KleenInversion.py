n, k = map(int, input().split())

A = list(map(int, input().split()))

MOD = 1000000007

ans = 0

for i in range(n) :
    contaf = 0
    contpre = 0
    for j in range(i, n) :
        if A[i] > A[j] : contaf += 1
    for m in range(0, n) :
        if A[i] > A[m] : contpre += 1

    ans += k*contaf%MOD
    ans%=MOD
    ans += ((k - 1) * k) / 2 % MOD * (contpre) % MOD;
    ans%=MOD

print(ans)