sd = input()
t = input()

ls = len(sd)
lt = len(t)

sd = list(sd)

s = []

tag = 0

for i in range(ls-lt, -1, -1) :
    ok = 1
    temp = sd[i:i+lt]
    #print (temp)
    for j in range(lt) :
        if temp[j] != "?" and temp[j] != t[j] : 
            ok = 0
    
    if ok :
        for j in range(lt) : 
            sd[i+j] = t[j]
        for j in range(ls) :
            if sd[j] == "?" : s.append("a")
            else : s.append(sd[j])
        tag = 1
        break

if tag :
    s = "".join(s)
    print(s)
else :
    print("UNRESTORABLE")