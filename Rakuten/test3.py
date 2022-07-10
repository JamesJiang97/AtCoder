def solution(A, B, C) :

    a = A
    b = B
    c = C

    alf = [['a', a], ['b', b], ['c', c]]

    alf = sorted(alf, key = lambda x : x[1], reverse= True)

    ans = ''

    while alf[0][1] + alf[1][1] + alf[2][1] : 
        if alf[1][1] :
            tag = 2
            while alf[0][1] and tag :
                ans += alf[0][0]
                tag -= 1
                alf[0][1] -= 1
            ans += alf[1][0]
            alf[1][1] -= 1
        else:
            tag = 2
            while alf[0][1] and tag :
                ans += alf[0][0]
                tag -= 1
                alf[0][1] -= 1
            break
        alf = sorted(alf, key = lambda x : x[1], reverse= True)            

    return ans 

A = 6
B = 1
C = 1

ans = solution(A, B, C)

print(ans)