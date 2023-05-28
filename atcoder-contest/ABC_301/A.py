n = int(input())
S = input()

T = 0
A = 0

for s in S:
    if s == 'T':
        T += 1
    else:
        A += 1
    if T == n/2:
        print('T')
        exit()
    elif A == n/2:
        print('A')
        exit()

if T > A:
    print('T')
else:
    print('A')