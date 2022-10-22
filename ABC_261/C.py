n = int(input())

count = [[0]* 10 **7 ] * 10**7

p = 131
#p1 = 193

mod = 393241
mod1 = 786433
# mod2 = 196613

for z in range(n) :
    s = list(input())
    hash = ord(s[0]) - 96
    hash1 = ord(s[0]) - 96
    # hash2 = ord(s[0]) - 96
    for i in range(1, len(s)) :
        S = ord(s[i]) - 96
        hash = (hash * p + S)%mod
        hash1 = (hash1 * p + S)%mod1
        # hash2 = (hash * p + S)%mod2
    if count[hash][hash1] :
        print(''.join(s) + '(' + str(count[hash][hash1]) + ')')
        count[hash][hash1] += 1
    else :
        print(''.join(s))
        count[hash][hash1] += 1

