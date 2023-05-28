n = int(input())

res = 0

for i in range(n):
    s = input()
    if s == 'For':
        res += 1

if res >= n/2 : print('Yes')
else : print('No')