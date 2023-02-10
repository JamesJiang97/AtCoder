import sys
sys.setrecursionlimit(2000)


s = input()
t = input()

lenth = len(t)

ans = 0

def binarySearch (l, r, S, T, ans): 
    mid = int(l + (r - l)/2)

    ans += mid
    ans = abs(ans)

    # print(S)
    # print(T)

    # 元素整好的中间位置
    if T[:mid] == S[:mid] and T[mid+1:] == S[mid:]: 
        return ans
       
    # 元素小于中间位置的元素，只需要再比较左边的元素
    elif T[:mid] != S[:mid]: 
        S = S[l: mid]
        T = T[l: mid]
        r = len(T) - 1
        return binarySearch(0, r, S, T, -ans) 

    # 元素大于中间位置的元素，只需要再比较右边的元素
    else: 
        S = S[mid: r]
        T = T[mid: r]
        r = len(T) - 1
        return binarySearch(0, r, S, T, ans) 

ans = binarySearch(0, lenth-1, s, t, ans) + 1

print(ans)
  