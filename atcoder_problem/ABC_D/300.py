import math

n = int(input())

def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes

max_c = math.ceil(math.sqrt(n/12))

primes = sieve_of_eratosthenes(max_c)

ans = 0

l = len(primes)

for i in range(len(primes)):
    k = l-1
    for j in range(i+1, min(k, l-1)):
        while j < k:
            v = primes[i]*primes[i]*primes[j]
            if v > n:
                k -= 1
                continue
            v *= primes[k]
            if v > n:
                k -= 1
                continue
            v *= primes[k]
            if v > n:
                k -= 1
                continue
            break
        ans += (k-j)

print(ans)


