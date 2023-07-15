S = str(input())
T = str(input())

SP = []
TP = []

SP.append([S[0],1])
TP.append([T[0],1])

for i in range(1, len(S)) : 
    if S[i] == S[i-1] : SP[-1][1] += 1
    else : SP.append([S[i], 1])

for i in range(1, len(T)) : 
    if T[i] == T[i-1] : TP[-1][1] += 1
    else : TP.append([T[i], 1])

tag = 1

ls = len(SP)
lt = len(TP)

for i in range(len(SP)) :
    if ls != lt :
        print('No')
        tag = 0
        break
    tp = TP[i]
    sp = SP[i]
    if sp[0] != tp[0] : 
        print('No')
        tag = 0
        break
    else :
        if tp[1] > sp[1] :
            if sp[1] == 1 :
                print('No')
                tag = 0
                break
        if sp[1] > tp[1] :
            print('No')
            tag = 0
            break


if tag :
    print('Yes')