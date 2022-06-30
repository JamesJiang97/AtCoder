def solution(A, K) :
    A.sort()
    ANS = [[A]]
    for i in range(1, K+1) :
        temp = []
        for j in ANS[i-1]:
            l = j.copy()
            r = j.copy()
            l.remove(j[0])
            r.remove(j[len(j)-1])
            temp.append(l)
            temp.append(r)
        ANS.append(temp)
    ans = []
    for i in ANS[len(ANS)-1] :
        ans.append(i[len(i)-1]-i[0])
    return(min(ans))
    print(min(ans))

A = [5,3,6,1,3]
K = 2

solution(A, K)
