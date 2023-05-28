n = int(input())

A = [list(input()) for i in range(n)]

flag = 1

for i in range(n-1) :
    if flag == 0 : break
    for j in range(i+1, n) :
        if A[i][j] == 'W' and A[j][i] != 'L' :
            flag = 0
            print('incorrect')
            break
        if A[i][j] == 'L' and A[j][i] != 'W' :
            flag = 0
            print('incorrect')
            break
        if A[i][j] == 'D' and A[j][i] != 'D' :
            flag = 0
            print('incorrect')
            break

if flag : 
    print('correct')                        

