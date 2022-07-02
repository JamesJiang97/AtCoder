n = int(input())

S = []

for i in range(n) : 
    l, r = map(int, input().split())
    S.append([l, 0])
    S.append([r, 1])

S = sorted(S)

tag = 0

for s in S : 
    if s[1] == 0 :
        if tag == 0 : 
            print(s[0], end = ' ')
        tag += 1
    else : 
        tag -= 1
        if tag == 0 : print(s[0])