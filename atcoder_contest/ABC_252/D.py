N = int(input())
A = list(map(int, input().split()))

UPPER=2*10**5
 
tag=[0]*(UPPER+1)

for i in A :
    tag[i] += 1

ans = 0
tag.remove(0)

for i in range(len(tag)) :
    for j in range(i+1, len(tag)) :
        for k in range(j + 1, len(tag)) :
            ans += tag[i]*tag[j]*tag[k]

print(ans)