S = input()
n = int(input())

l  = len(S)

indx = []

reS = list(S[::-1])

numS = reS

for i in range(l):
    if reS[i] == '?':
        indx.append(i)
        numS[i] = '0'

if int("".join(numS[::-1]), 2) > n:
    print(-1)
    exit()

for i in reversed(indx):
    numS[i] = '1'
    if int("".join(numS[::-1]), 2) <= n:
        continue
    else:
        numS[i] = '0'

print(int("".join(numS[::-1]), 2))





