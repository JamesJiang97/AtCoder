n, q = map(int, input().split())
s = str(input())
one = 0
Q = [list(map(int, input().split())) for i in range(q)]
ls = q
i = 0
while(i < ls) :
    if Q[i][0] == 1 :
        while Q[i+1][0] == 1 :
            Q[i][1] += Q[i+1][1]
            Q[i][1] %= n
            del(Q[i+1])
            ls -= 1
    if Q[i][0] == 2 :
        while Q[i+1][0] == 2 :
            Q[i].append(Q[i+1][1])
            del(Q[i+1])
            ls -= 1
    i += 1

for q in Q :
    t = q[0]
    if t == 1 :
        one = q[1]
        temp = s[n-one:n]
        s = temp + s[:n-one]
    if t == 2 :
        l = len(q)
        for i in range(1, l) : 
            print(s[q[i]])
