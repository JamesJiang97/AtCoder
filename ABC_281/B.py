S = input()

l = len(S)

if l != 8:
    print("No")
else:
    s1 = S[0]
    s2 = S[1:7]
    s3 = S[7]
    if s1.isdigit() == False and s2.isdigit()==True and s3.isdigit() == False :
        if int(s2) >= 100000 :
            print("Yes")
        else:print("No")    
    else : print("No")