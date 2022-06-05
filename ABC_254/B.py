n = int(input())

ans = [[]]

ans[0].append(1)


for i in range(1, n) :
    temp = []
    for j in range(0, i+1) :
        if j == 0 or j == i : temp.append(1)
        else :
            temp.append(ans[i-1][j-1] + ans[i-1][j])

    ans.append(temp)


for i in range(n) :
    for j in ans[i] :
        print(j, end = " ")
    print("\n")