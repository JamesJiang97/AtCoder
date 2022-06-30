def solution(S, P, Q) :
    A = [0] * 100000
    C = [0] * 100000
    G = [0] * 100000
    T = [0] * 100000

    ans = [4] * len(P) 

    for i in range(len(S)) :
        if S[i] == 'A' : A[i] = A[i-1] + 1
        elif S[i] == 'C' : C[i] = C[i-1] + 1
        elif S[i] == 'G' : G[i] = G[i-1] + 1
    
    for i in range(len(P)) :
        p = P[i]
        q = Q[i]
        if A[q] - A[p-1] : ans[i] = 1
        elif C[q] - C[p-1] : ans[i] = 2
        elif G[q] - G[p-1] : ans[i] = 3
    
    return ans
