x, y, z = map(int, input().split())

if abs(z) > abs(y) and ((z>0 and y>0 and x>0)or(z<0 and y<0 and x<0)) and abs(y) < abs(x): print(-1)
else : 
    if abs(x) < abs(y) or  (x < 0 and y > 0) or (x>0 and y < 0) : print(abs(x))
    else :
        if (x < 0 and z > 0) or (x>0 and z < 0) : print(2*abs(z) + abs(x))
        else : print(abs(x))