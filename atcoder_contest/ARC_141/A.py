t = int(input())

for z in range(t) :
    s = input()
    ns = int(s)
    l = len(s)
    divisor = []
    for i in range(1, l) :
        if l % i == 0 : divisor.append(i)
    
    res = []
    for d in divisor :
        temp = []
        if s[0:d] == 1 :
            temp.append("9"*(l-1))
            temp.append("1"*l)
        else :
            temp.append(s[0:d]*(l//d))
            temp.append(str(int(s[0:d])-1)*(l//d))
        for i in range(len(temp)) :
            if int(temp[i]) > ns :
                temp[i] = "-1"
        
        res += temp
                            
    
    ans = []
    for i in res :
        ans.append(int(i))
    print(max(ans))




