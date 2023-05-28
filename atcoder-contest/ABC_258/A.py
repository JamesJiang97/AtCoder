k = int(input())

if k >= 70 : print("22:" + str(k-60))
elif k >=60 : print("22:0" + str(k-60))
elif k < 10 : print("21:0" + str(k))
else : print("21:" + str(k))
