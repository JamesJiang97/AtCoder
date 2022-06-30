def solution(A, K) :
    ans = []

    for i in range(len(A)-K+1) :
        temp = A.copy()
        for j in range(i, i+K) :
            temp[j] = 0
        temp.sort()
        ans.append(temp[len(temp)-1]-temp[0])
    
    print(ans)
    return(min(ans))


A = [5,3,6,1,3]
K = 2

print(solution(A, K))
