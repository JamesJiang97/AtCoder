for i in range(1,10):
    s  = str(i)*5
    for j in range(5):
        s += str(i)*j
        if int(s) % 12056 == 0:
            print(s)