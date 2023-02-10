n = 1027026000

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

li = make_divisors(1027026000)

ans = 0

for i in li:
    if i >=10000 and i <= 99999:
        ans += i
    if i > 99999 :
        break

print(ans)