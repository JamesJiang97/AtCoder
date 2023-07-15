x, a, d, n = map(int, input().split())

upper = a + d*(n-1)

if (x < a and x <upper) or (x>a and x > upper) : print(min(abs(x-a), abs(x-upper)))
else : 
    if x == a : print(0)
    else:
        dis = abs(x-a)%abs(d)
        dis = min(dis, abs(d) - dis)
        print(dis)

