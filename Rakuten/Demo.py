def solution(A):
    lena = 1000000
    bucket = [0] * (lena + 2)
    for n in A :
        if(n > 0) :
            bucket[n] = 1
    for i in range(1, len(bucket)) :
        if bucket[i] == 0 : return i
    
A = [-1,-3]

print(solution(A))