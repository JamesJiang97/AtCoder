import bisect


q = int(input())

s = []

for w in range(q) :
    inp = list(map(int, input().split()))
    if inp[0] == 1 :
        u =  bisect.insort_left(s, inp[1])
    elif inp[0] == 2 and s.count(inp[1])!=0:
        temp = min(inp[2], s.count(inp[1]))
        posi = s.index(inp[1])
        for i in (posi, posi + temp) :
            del s[posi]
    elif inp[0] == 3 :
        print(s[len(s)-1] - s[0])
