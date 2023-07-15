n, k = map(int, input().split())

list = []

for i in range(n):
    a, b = map(int, input().split())
    list.append([a, b])

list = sorted(list, key=lambda x: x[0], reverse=True)
list.append([0, 0])

# print(list)


ans = [list[0][0] + 1, 0]

for i in range(1, n+1):
    # print(ans)
    f = ans[1] + list[i-1][1]
    if f > k:
        print(ans[0])
        exit()
    else:
        ans[1] = f
        ans[0] = list[i][0] + 1

print(ans[0])
    
