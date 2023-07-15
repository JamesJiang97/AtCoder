    l = len(base10int(n,3))
    if k >= l and k<= n and (l+k)%2 == 0:
        print("Yes")
    else:
        print("No")