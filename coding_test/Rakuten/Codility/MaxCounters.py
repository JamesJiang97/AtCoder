def solution(N, A) : 

    ANS = [0] * N 
    maxcounter = 0 
    minvalue = 0 
    for n in A : 
        if n == N+1 : 
            maxcounter = max(ANS)
        else :
            if ANS[n-1] < maxcounter :
                ANS[n-1] = maxcounter + 1
            else :
                ANS[n-1] += 1

    for i in range(len(ANS)) :
        if ANS[i] < maxcounter :
            ANS[i] = maxcounter
    return ANS

A = [3,4,4,6,1,4,4]
N = 5
print(solution(N, A))