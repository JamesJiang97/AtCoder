n = int(input())

l = 1
r = n

for i in range(20):
    m = (l+r)//2
    print("?"+str(m))
    s = int(input())
    if s :
        r = m
    else:
        l = m
    if r == l+1:
        print("!"+str(l))
        exit()

