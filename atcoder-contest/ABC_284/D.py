import collections

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n and len(a) < 3:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

t = int(input())

for i in range(t):
    A = collections.Counter(prime_factorize(int(input())))
    q = 0
    p = 0
    for a in A:
        if A[a] == 1:
            q = a
        else: p = a
    print(str(p) + " " + str(q))