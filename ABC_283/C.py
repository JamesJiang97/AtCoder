import math


S = input()

res = 0

i = 0

l = len(S)

while i < l:
    # print(S[i] + " " + S[i+1])
    if i != l-1:
        if S[i+1] == '0':
            res += 1
            i += 1
            t =[]
            while S[i] == '0':
                t.append(S[i])
                i += 1
                if i == l:
                    break
            res += math.ceil(len(t)/2)
        else: 
            res += 1
            i += 1
    else:
        res += 1
        i += 1
    # print(res)

print(res)
